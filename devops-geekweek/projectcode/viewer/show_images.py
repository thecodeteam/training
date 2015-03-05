from flask import Flask, render_template #import our web server
import logging #with loggins

import redis #and redis
from config import Config # and the config files
import os #and some OS functions

cfg = Config(file('private_config.cfg'))
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s [%(module)s:%(funcName)s] [%(levelname)-5.5s] %(message)s")
# loggly_handler = loggly.handlers.HTTPSHandler(url="{}{}".format(credentials["Loggly"]["url"], "gui"))
# loggly_handler.setLevel(logging.DEBUG)
# logger.addHandler(loggly_handler)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.WARN)
#setup logging, check twitter_watch for details on what all the above does.


#setup flask
app = Flask(__name__)

#connect to redis
redis_images = redis.Redis(host=cfg.redis_host,db=cfg.redis_images_db, password=cfg.redis_password)

#gets a list of random URLS from refis.
def get_random_urls(count=100):
    pipe_keys = redis_images.pipeline() #setup 2 batches
    pipe_urls = redis_images.pipeline()
    keys = []
    for i in range(0,count): # get 'count' random keys
        pipe_keys.randomkey()

    for key in pipe_keys.execute(): #for each one of those random keys
        pipe_urls.hget(key,"url") #get the URL property.

    urls = pipe_urls.execute() #the list of URLs is the result.
    return urls #return it.


#This responds to requests for "/"
@app.route('/')
def dashboard():
    urls = get_random_urls() # get the list of URLs
    return render_template('default-us.html',urls=urls) #Responsed by feeding that list of URLs into the template, and returning the rendered HTML

if __name__ == "__main__":
    port = int(os.getenv('VCAP_APP_PORT', '5000')) #liston in VCAP_APP_PORT if known, otherwise 5000
    logging.info("Running on port {}".format(port))
    app.run(host='0.0.0.0', port=port) #listen on specific port and all IP addresses.
