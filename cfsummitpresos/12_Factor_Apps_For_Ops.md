^ build-lists: true
^ Open this presentation with [Deckset](http://www.decksetapp.com/)


![fit] (images/title.jpg)

---

![fit] (images/speakers.jpg)


# 12 Factor Apps for Operations

### rags srinivas (@ragss)
### matt cowger (@mcowger)

---

>http://12factor.net

---

> I didn't change anything!
-- every. developer. ever.

---

> Well the environment didn't change!
-- every. ops. person. ever.

---

# \#1: Codebase

* Everything in revision control
  * Including environment configuration

^ Matt

---

# Revision Control -> `git blame`
#####(`svn blame` if you must)

^ Matt

---

![fit] (http://memecrunch.com/meme/ZEUJ/if-you-bothered-to-look-at-git-blame/image.jpg)

---

# \#2: Dependencies

* Dependencies must be explicitly declared
* They should be declared with the rest of the code, and tracked the same way
* Dependencies tracking should contain version numbers of dependencies

---

![fit] (https://thisistwitchy.files.wordpress.com/2012/11/passing-the-buck.jpg)

^Matt - If it wasn't documented, how could you know it even was a requirement?  if it doesn't exist in SCM, it doesn't exist.

---

![fit] (http://net-informations.com/faq/framework/img/obsolete.png)

^Matt - Version everything. Deprecated functions means version numbers are critical.  Image courtesy: http://blog.simpsn.com/replacing-deprecated-functions-in-phpthumb-to-be-compatible-with-php-version-5-3-0

---

# \#3: Config

* Config belongs in the environment if possible - it varies between deploys, but the code doesn't
* Includes access credentials, logging config, etc.
* Should be read at runtime, not preprocessed into code.

^Matt - config, especially passwords, suck.

---

![fit] (images/configshuffle.png)

^Matt - this is a recipe for horribleness.  

---

* Only people with access to host & account can see creds
* Creds can be specific (maybe avoid shared accounts!)
* Now everyone knows the live config, all the time, and be sure code is using it.
* Less danger of having critical file stolen/checked in

---

![fit] (images/yaml.jpg)

---

# \#4: Backing Services

* Anything your application uses as a resource (database, queueing system, email, cache) should be referenced with 'bindings' to these services.
* All applications deployed with explicit declarative references ( as in manifest.yml)
* Avoid implicit references (User Provided Services)

^Rags - Explicitly declared. Access methods must be declared as well. Put everything in YAML, for example 


---

![fit] (images/profiles.jpg)

---

# \#5: Build Release Run

* Build, Release and Run are separate stages for the application life cycle.
* Version everything
* Use profiles
* Blue/Green Deployments are a rule, not an exception.


^Rags - Everything is code. Infrastructure is code. Data is code. If it's manual it's broke. If it's not versioned it's broke. This is related to #3 - config

---

![fit] (images/bellichick.jpg)

^ Image courtesy: pintrest.com

---

# \#6: Processes

* Seperation of concerns - each microservice is a single process
* Instances of running code to be stateless - certain exceptions apply
* This makes apps more resilient, and easier to recover
* Categorize processes into Stateful and Stateless

^Rags - The Unix principle. Stateless - no problem. Treat Stateful processes or services differently.

---
# \#7: Port Binding

* Export services via port binding
* For instance HTTP is exported as a service via port binding and not injected at run time.
* The ultimate goal is to be able to horizontally scale.


^Rags -  CF, Lattice and Containers deal with this for the most part. Don't always assume that MySQL runs on 3306 or Couchbase runs on 8091.

---

# \#8: Concurrency

* An extension of # 6 above.
* An implication to scale out.
* Not necessarily required for certain aspects (single process workers, etc)

^Rags -- Application locking and concurrency built in.

---

![fit] (images/concurrency.png)

^ `http://12factor.net/concurrency`

---

# \#9: Disposability

* Losing a process should be a normal event
* No loss of state for user if we lose a process
* Startup times should be low
* Platforms can adapt to errant processes and self heal if required.

^Rags

---

![fit] (http://upload.wikimedia.org/wikipedia/en/thumb/d/de/Cat-Cute-Kitten-HD-Wallpaper.jpg/1024px-Cat-Cute-Kitten-HD-Wallpaper.jpg)
![fit] (http://img.photobucket.com/albums/v453/jmr8891/Silkies/Misc/IMG_7264.jpg)

^ Image courtesy: http://www.slideshare.net/gmccance/cern-data-centre-evolution

---

![fit] (images/workedonmine.jpg)

---

# \#10: Dev / Prod Parity

* Dev MUST == Production in config, but not performance
* Following the above helps do this

---

![fit] (images/worksonmymachine.png)


---

# \#11: Logs

---

![fit] (images/criticalerror.png)

---

* Log *everything*
  * Storage is cheap
  * Searching is cheap
* Logs help fix problems *after* they happen
* Use tokens for specific flows


---

![fit] (images/rca.jpg)

---

# Measure/Monitor Everything

---

![fit] (images/pcfopsmanager.tiff)

---

# \#12: Admin Processes

* Use your app/framework for these... build in the tools as needed.
* Don’t run updates directly against a database
* Don’t run them from a local terminal window
* ChatOps can help here


---

# More Resources

* [Systems that Never Stop] (http://www.infoq.com/presentations/Systems-that-Never-Stop-Joe-Armstrong) 
* [Pivotal Podcasts: Episode 23 (Operational transformation) ](http://blog.pivotal.io/podcasts-pivotal) 
* [You Build it, you run it - an interview with Werner Vogels] (https://queue.acm.org/detail.cfm?id=1142065)
* [This presentation] (https://github.com/emccode/training/blob/master/cfsummitpresos/)







