(open this document in http://stackedit.io to see the diagrams rendered)

#Documentation for Project Vasco da Gama
---
##Purpose
The purposes of Project VdG is to demonstrate the nexus of a number of products in the EMC federation.  Specifically, the things we are trying to demonstrate are:

* Pivotal CloudFoundry
  * CF scaling capabilities
  * CF deployment capabilities
* EMC ViPR Object Store
  * ViPR supports S3-style object access
* Redis NoSQL Database
  * (Redis development is supported by Pivotal)

The application displays a random subset of tweet images to the user upon request, after collecting and storing them in a scalable way.

---
##Components
### Twitter Watcher
####Description
Specifically, the application requests a stream of tweets from Twitter using the streaming API (which gives us about 1% of the feed) that match some given hash tags.  For every tweet received, we check for an attached image, and if it has one, we dispatch a job into a job queue for processing.  In that job, the following actions are performed:

1. The tweet image is retrieved from the web
2. The image undergoes some processing (currently a simple blur, but its demonstrative of other things that could be done, such as face recognition)
3. The image is stored into the ViPR object store
4. The image metadata is stored into Redis

The code for this part of the module is found in the `twitter_watch` subdirectory, and can be executed with `python run.py` from the main code directory.  

Additionally, there are 1 or more workers that must be deployed and which receive jobs from the job queue for execution.  These are called `rqworkers`, and can be executed by running `rqworker -u redis://:<password>@<hostname>/3 default dashboard` from the same directory as the remainder of the code.  The number of workers deployed may be increased from a minimum of 1 to a maximum of at least 100 (although no more than 20 have been tested, the larger job queue system in use, called RQ, has been tested with hundreds).  Overall its been found that about 5 workers are sufficient to handle the load.

A sequence diagram follows.

####Data Collection Sequence :
```sequence
Twitter->Twitter Watcher: Here is a Tweet for You
Twitter Watcher->Redis RQ: Here's an image URL to queue
Redis RQ->Redis DB: Here's a job to store.
Redis DB-->Redis RQ: Got it, thanks
Redis RQ-->Twitter Watcher: I got it, thanks
Twitter Worker->Redis RQ: Do you have any work for me?
Redis RQ-->Twitter Worker: I sure do, here's a URL
Twitter Worker->Twitter Image Server: Gimme that Image!
Twitter Image Server-->Twitter Worker: Fine! So needy!
Note over Twitter Worker: Performs image manipulation
Twitter Worker->ViPR Object: Please store this image, and delete it in 1 day
ViPR Object-->Twitter Worker: Done
Twitter Worker->ViPR Object: Please give me a public URL for this image
ViPR Object-->Twitter Worker: <URL>
Twitter Worker->Redis DB: Please store a record of this image and its URL and size. Delete the record in 1 day
Redis DB-> Twitter Worker: Done
Twitter Worker-->Redis RQ: My Job is Complete, Here's the Result
Redis RQ-->Redis DB: Store this Job Result, and Mark it Complete
Redis DB-->Redis RQ: Done!
```

### Twitter Dashboard
####Description
A second component to the application is generation of the [dashboard](https://freeboard.io/board/kofu1K), specifically the data that feeds that dashboard.  This is the responsbility of the dashboard part of the application found in the `dashboard` directory, and executable with `python run_dashboard.py`.  Its operation consists of gather a number of statistics from Redis, ViPR and the job queue and adds jobs to the queue to upload that data.

The actual jobs to upload the data are simple calls into a service called [Dweet](http://dweet.io), which is styled as a 'Twitter for Devices', and accepts updated in a streaming fashion, making them available to other services like Freeboard.

The workers can be started similarly to the watcher workers described above, and we recommend having at least 1 dedicated worker: `rqworker -u redis://:<password>@<hostname>/3 dashboard`


####Dashboard Generation
```sequence
Dashboard App->Redis RQ: Give me some stats
Redis RQ-> Dashboard App: Here's some
Dashboard App->Redis DB: Give me some stats
Redis DB-> Dashboard App: Here's some
note over Dashboard App: Some internal cleanup of the data
Dashboard App->Redis RQ: Here's some data to post to Freeboard.io
Redis RQ-->Dashboard App: Understood and stored.
Dashboard Worker->Redis RQ: Do I have any work to post?
Redis RQ--> Dashboard Worker: Sure, here you go.
Dashboard Worker->Freeboard: Here's some metrics, buddy
Dashboard Worker-->Redis RQ: I'm done
Note over Dashboard App: Sleep 10 seconds and repeat
```

### Twitter Visualization
####Description
The final and clearest interaction a user has with the application is to access its UI via a standard web browser.   Upon connection to the server (which is contained in `viewer`, and executed with `python viewer/show_images.py`), the user receives a page designed by the brilliant [Kenny Coleman](http://kendrickcoleman.com) which displays a set of 100 images, randomly selected from the Redis database and served directly from ViPR object.

A new set of images are chosen on each page load.

Intentionally, very little work is done in the UI side of the application to keep it simple and scalable.

####UI Visualization
```sequence
User->UI: GET /
UI->Redis: Give me 100 random keys from the database.
Redis-->UI: Here!
UI->Redis: For each one of these keys, gimme the URL
Redis-->UI: Here!
UI->User: Here's a page, with 100 URLs filled in.
User->ViPR Object: Gimme these images
ViPR Object-->User: Here they are
Note over User: Gasp!  Its beautiful!
```

### Twitter Scaling
####Description
A huge part of the demonstration is to show how quickly and easily applications like this can be scaled.  As a result, a 'scaling controller' was written (code: `scaler`  execute: `python scaler/__init__.py`) to accept requests via a REST API, and cause the CloudFoundry CloudController to change the number of running instances.  This is used to change the number of Twitter Watcher workers on the fly and on demand.  

Conccurently, a demonstration iOS app wa written to utilize this REST API, and its code is available at TODO.


####Scaling Controller
```sequence
participant iPhone App
Scaling App->CloudController: Login
CloudController-->Scaling App: Done, here's a token. Don't lose it.
Scaling App->CloudController: What apps do I have access to?
CloudController-->Scaling App: These ones: [a,b,c]
iPhone App->Scaling App: Hey, here's my login, what apps are there?
Scaling App->iPhone App: Here's a list: [a,b,c]
note over iPhone App: User selects app, and scale target
iPhone App->Scaling App: Scale app named "a" to "n"
Scaling App->iPhone App: Understood
Scaling App->CloudController: scale app A to 'N'
```

### Other Components
####Cloud Foundry Manifest
The Cloud Foundry configuration can be easily predefined, and this is done so in the `manifest.yml` file, which defines the various components and their requirements.  A sample follows:

```
- name: twitter-scaler #name of the application
  memory: 128M         #How much memory to allocate to the service.
  no-route: false      #make sure this is publicly listening
  instances: 1         #start with 1 instances of the service
  buildpack: python_buildpack  #which CF build pack should be used?
  command: python scaler/__init__.py #how to execute the service
```

####rqinfo
RQ includes a tool to watch the state of workers and the job queues.  It can be executed from within the directory with the following: `rqinfo --interval 3 -u redis://:<password>@<hostname>/3`

####requirements.txt
All python requirements for the application can be found in `pip` format in `requirements.txt`.  You can install all of them (best if done inside a `virtualenv`) with `pip install -r requirements.txt`