
from config import Config #config file module
import logging #standard logging
import redis #interaction with redis
from memoize import Memoizer #memoization is a method of caching function results.
from rq import Queue #RedisQ, our job management system
from pprint import pprint, pformat #pretty print
import datetime #date/time utils
import time #time utils
from rq.decorators import job #funtion decoration
import dweepy #see dweet.io






cache_store = {} #Where will we cache results.  Just use an inmemory dictionary.  If we wanted to scale bigger, what could we use?
memo = Memoizer(cache_store) #Use that.
max_cache_time = 2 #But only keep results for 2 seconds.


logger = logging.getLogger('')
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(module)s:%(funcName)s] [%(levelname)-5.5s] %(message)s")
# loggly_handler = loggly.handlers.HTTPSHandler(url="{}{}".format(credentials["Loggly"]["url"], "gui"))
# loggly_handler.setLevel(logging.DEBUG)
# logger.addHandler(loggly_handler)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.WARN)
###Setup all our logging, see twitter_watch for more details.




cfg = Config(file('private_config.cfg'))
r = redis.Redis(
    host=cfg.redis_host,
    db=cfg.redis_rq_db,
    password=cfg.redis_password
)

redis_images = redis.Redis(
    host=cfg.redis_host,
    db=cfg.redis_images_db,
    password=cfg.redis_password
)
q = Queue(connection=r)

#Setup our redis and RQ connections.   see twitter_watch for more details.


@job("dashboard", connection=r, timeout=3)
def send_update(metric, value): #method for sending updates about metrics as needed.
    logger.info("Sending update for {}".format(metric))
    dweepy.dweet_for(cfg.dweet_thing, {metric: value})

def update_dashboard(): # the primary function.
    logger.info("updating")


    #For each one of the metrics, collected the data and issue a job to actually send that out.

    tweets_in_queue = get_queue_len()
    logger.info("Sending update for {}".format("tweets-in-queue"))
    send_update.delay("tweets-in-queue",tweets_in_queue)
    #dog.metric('tweets.inqueue', tweets_in_queue, host="twitter")

    time_in_q = get_time_in_q()
    logger.info("Sending update for {}".format("time-in-queue"))
    send_update.delay("longest-time-in-queue", time_in_q)
    #dog.metric('tweets.timeinqueue', time_in_q, host="twitter")

    worker_count = get_worker_count()
    logger.info("Sending update for {}".format("worker-count"))
    send_update.delay("worker-count",worker_count)
    #dog.metric('workers.count', worker_count, host="twitter")


    size, count = get_image_stats()
    logger.info("Sending update for {}".format("image-size"))
    send_update.delay("images-size", size)
    #dog.metric('images.size', size, host="twitter")

    logger.info("Sending update for {}".format("key-in-redis"))
    send_update.delay("keys-in-redis", count)
    #dog.metric('images.count', count, host="twitter")

    ops_per_sec = get_ops_per_sec()
    logger.info("Sending update for {}".format("ops-per-sec"))
    send_update.delay("ops",ops_per_sec)
    #dog.metric('redis.inqueue', ops_per_sec, host="twitter")

    exec_time = get_exec_time()
    logger.info("Sending update for {}".format("execution time"))
    send_update.delay("execution-time",exec_time)
    #dog.metric('tweets.execution_time', exec_time, host="twitter")

    tweet_count = get_tweet_count()
    logger.info("Sending update for {}".format("total tweets"))
    send_update.delay("tweet-count",tweet_count)
    #dog.metric('tweets.count', tweet_count, host="twitter")

    tweets_processed = get_tweets_processed()
    logger.info("Sending update for {}".format("total tweets processed"))
    send_update.delay("tweet-processed",tweets_processed)
    #dog.metric('tweets.processed', tweets_processed, host="twitter")



def get_worker_count():

    return len(r.smembers("rq:workers"))-1
    #The number of workers is 1 less than the members in the rq:workers set (because 1 worker is dedicated to just dashboards)

def get_image_stats():

    total_count = 0
    total_size = 0

    tx = redis_images.pipeline() #because this is going to be a bunch of operations, we do this in a pipeline.

    for key in redis_images.keys(): #for every key in Redis (yes, thats expensive and could be tens of thousands of keys)
        total_count += 1 #keep track of how many there are.
        tx.hget(key,"size") #and for each one get the size.

    for result in tx.execute(): #Now we execute that batch jobs, and the results come back in a list.  For each one
        if result:
            total_size += int(result) #Add it to the total size after converting to integer (Redis stores everything as a string)

    total_size = round(total_size / 1024 / 1024) #Turn that into MB

    return int(total_size), int(total_count) #and return both!

def get_ops_per_sec():
    return int(r.info()['instantaneous_ops_per_sec']) #Get this from the Redis status

def get_queue_len():
    return len(q) #Easy way to determine number of jobs in queue.

def get_time_in_q():

    try:
        oldest_job = q.jobs[0] #find the oldest job (because its at queue position 0)
        enqueued = oldest_job.enqueued_at #find out when it was enqueues
        now = datetime.datetime.utcnow() #when is it now
        delta = (now-enqueued).seconds #whats the delta
        return delta #and return it
    except IndexError as e:
        #Queue was empty if we got here, so the oldest value is 0
        return 0

def get_exec_time():
    count = r.llen("stats:execution-times") #We keep the execution times in a Redis List.  Found out how many entries we have
    if count == 0: #if there are none, return 0
        return 0.0
    total = 0 #other wise, for each value, add it up.
    for exec_time in r.lrange("stats:execution-times",0,count):
        total += float(exec_time)


    average = float(total)/count #and calculate the average.
    r.ltrim("stats:execution-times",0,0) #delete all the entries so its clean for next time.
    return round(average,2) #Return the average.

def get_tweet_count():
    return int(r.get("stats:tweets")) #simple get from redis

def get_tweets_processed():
    return int(r.get("stats:tweets-processed")) #simple get from redis.


if __name__ == "__main__":
    while True:
        update_dashboard() #Run the updates
        time.sleep(10) #sleep for 10 seconds
