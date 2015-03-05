from __future__ import print_function #force the use of print(X) rather than print X
from config import Config #import a module that makes config files easier
from TwitterAPI import TwitterAPI #The twitter API
from PIL import ImageFilter, Image #The Python Imaging Library
from StringIO import StringIO #StringIO lets you treat a string in memory like a file handle
import requests #request is a great library for interacting with web services
from pprint import pprint,pformat #pprint can pretty print complex data structures
import logging #the standard python logging library
import boto # the library for interacting with AWS services
from boto.s3.key import Key #Class to represent a S3 key
from boto.s3.lifecycle import Lifecycle, Expiration #classes so we can set lifecycles/expirations on objects
import time #basic time handling library
import redis #redis library
import uuid #library for creating unique IDs
import random #lirbary for random numbers
from log_with import log_with #library for making some kinds of logging easier
from rq import Queue #RQ, the job queueing system we use
from rq.decorators import job #And the function decoration for it.
import dweepy #the library we use for sending status updates.  Check http://dweet.io

logger = logging.getLogger('') #Grab the logging instance for our app, so we can make changes
logger.setLevel(logging.DEBUG) # LOG ALL THE THINGS!
formatter = logging.Formatter("%(asctime)s [%(module)s:%(funcName)s] [%(levelname)-5.5s] %(message)s")
#and make them look prettier

ch = logging.StreamHandler() #set up a logging handler for the screen
ch.setLevel(logging.INFO) #make it only spit out INFO messages
ch.setFormatter(formatter) #make it use the pretty format
logger.addHandler(ch) #and finally add it to the logging instance

logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.WARN)
#From this particular library, supress certain messages.


cfg = Config(file('private_config.cfg')) #import our configuration file

#setup a connection to redis for the images database (Redis can have multiple databases)
redis_images = redis.Redis(host=cfg.redis_host,db=cfg.redis_images_db, password=cfg.redis_password)

#Setup a connection that will be used by RQ (each redis connection instance only talks to 1 DB)
redis_queue = redis.Redis(
    host=cfg.redis_host,
    db=cfg.redis_rq_db,
    password=cfg.redis_password
)

#Based on that connection, setup our job queue, and set async=True to tell it we want to run jobs out-of-band.
#We could set it to 'True' if we wanted it to run jobs right away.  Sometimes useful for debugging.
q = Queue(connection=redis_queue, async=True)


@job("dashboard",connection=redis_queue,timeout=10) #When this is run as a job, use apecific queue (dashboard) with specific timeouts.
def send_update(metric, value):
    """
    Accepts a metric name and a value, and sends it dweet.io
    """
    dweepy.dweet_for(cfg.dweet_thing, {metric: value})


@log_with(logger)
def get_image(image_url):
    """
    This is the job that gets queued when a tweet needs to be analyzed
    """
    start = time.time() #Lets store some timing info
    image = retrieve_image(image_url) #Go get that image
    if image is not None: #As long as we have a vaid image and its not None (aka Null)
        image = process_image(image) #Do our image processings
        if cfg.actually_store: #If our configu file says to store the image for reals
            key = store_to_vipr(image) #store to vipr
            store_to_redis(key) #and keep track of it in redis
    end = time.time() # and record how long it took
    if random.randint(1,10) < 5: #about 50% of the time we should
        redis_queue.lpush("stats:execution-times",end-start) #send in an update on execution time
    redis_queue.incr("stats:tweets-processed") #and also record that we processed another tweet.


@log_with(logger)
def store_to_redis(image_key):
    """
    Keep track of an image in redis
    """

    tx = redis_images.pipeline() #Because we are goign to do a bunch of Redis ops quickly, setup a 'pipeline' (batch the ops)
    tx.hset(image_key.key,"filename",image_key.key) #using the key's UUID as the name, set the hash value of 'filename' to the filename
    tx.hset(image_key.key,"url",image_key.generate_url(60*60*23)) #Get a URL, and store it.  That URL is good for 23 hrs
    tx.hset(image_key.key,"size",image_key.size) #Store the size of the image.  Better to store it here where its cheap to check than in ViPR where its expensive.
    tx.expire(image_key.key,60*60*23)  # Expire the entire redis key in 23 hours

    tx.execute() #Run the transaction.
    logger.info("Stored image to redis: {}".format(image_key))


@log_with(logger)
def process_image(image, random_sleep=1):
    image = image.filter(ImageFilter.BLUR) #run the image through a blur filter
    final_image = StringIO() #and now, since the PIL library requires a 'file like' object to store its data in, and I dont want to write a temp file, setup a stringIO to hold it.
    image.save(final_image, 'jpeg') #store it as a JPG
    if random_sleep: #added a random sleep here to make it seem like the process takes longer.  Simulates more expensive processing.
        time.sleep(random.randint(1, random_sleep))
    return final_image #and give back the image


@log_with(logger)
def retrieve_image(image_url):
    """
    Retrieves the image from the web
    """
    http = requests.session()
    logger.info("Capturing Image {}".format(image_url))
    im = None
    try:
        im = Image.open(StringIO(http.get(image_url).content)) #Try to get the image, but if it fails
    except IOError as e:
        logger.critical(e) ##Record what happened and return a None
        return None
    logger.info("Image Captured: {}".format(im))
    return im


@log_with(logger)
def store_to_vipr(image_data):
    logger.debug("Storing to ViPR")
    logger.debug("Connecting to ViPR")
    s3conn = boto.connect_s3(cfg.vipr_access_key, cfg.vipr_secret_key, host=cfg.vipr_url) #set up an S3 style connections
    logger.debug("Getting bucket")
    bucket = s3conn.get_bucket(cfg.vipr_bucket_name) #reference to the S3 bucket.
    lifecycle = Lifecycle() #new lifecycle managers
    logger.debug("Setting Bucket RulesViPR")
    lifecycle.add_rule('Expire 1 day', status='Enabled',expiration=Expiration(days=1)) #make sure the bucket it set to only allow 1 day old images.  Probably dont need to do this every time.  TODO!

    image_guid = str(uuid.uuid4()) #Pick a random UUID!
    k = Key(bucket) #and gimme a new key to refer to file object.
    k.key = "{}.jpg".format(image_guid) #give it a name based on the UUID.
    logger.debug("Uploading to ViPR")
    k.set_contents_from_string(image_data.getvalue()) #upload it.
    logger.info("Stored image {} to object store".format(k.key))
    return k #and return that key info.


@log_with(logger)
def watch_stream(every=10):
    twitter_api = TwitterAPI(
        consumer_key=cfg.twitter_consumer_key,
        consumer_secret=cfg.twitter_consumer_secret,
        access_token_key=cfg.twitter_access_token,
        access_token_secret=cfg.twitter_token_secret
    ) #setup the twitter streaming connectors.
    tweet_stream = twitter_api.request('statuses/filter', {'track': cfg.hashtag}) #ask for a stream of statuses (1% of the full feed) that match my hash tags
    for tweet in tweet_stream.get_iterator(): #for each one of thise
        logger.info("{}: Tweet Received") #Log it
        redis_queue.incr("stats:tweets") #Let Redis know we got another one.
        if not tweet['retweeted'] and 'entities' in tweet and 'media' in tweet['entities'] and \
                tweet['entities']['media'][0]['type'] == 'photo': #As long as it has all the right properties and has a photo.
            logger.info("Dispatching tweet with URL {}".format(tweet['entities']['media'][0]['media_url'])) # log it
            q.enqueue(
                get_image,
                tweet['entities']['media'][0]['media_url'],
                timeout=60,
                ttl=600
            ) #add a job to the queue, calling get_image() with the image URL and a timeout of 60s
