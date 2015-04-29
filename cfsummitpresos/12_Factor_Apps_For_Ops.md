build-lists: true
^ Open this presentation with [Deckset](http://www.decksetapp.com/)


![fit] (images/title.jpg)

---

![fit] (images/speakers.jpg)


# 12 Factor Apps for Operations

### rags srinivasan (@ragss)
### matt cowger (@mcowger)

---

# \#1: Codebase

* Everything in revision control
  * Including environment configuration

^ Matt

---

> I didn't change anything!
-- every. developer. ever.

---

> Well the environment didn't change!
-- every. ops. person. ever.

---

# Revision Control -> `git blame`
#####(`svn blame` if you must)

^ Matt

---

# \#2: Dependencies

* Dependencies must be explicitly declared
* They should be declared with the rest of the code, and tracked the same way
* Dependencies tracking should contain version numbers of dependencies

---

![fit] (images/obama.jpg)

^Matt - If it wasn't documented, how could you know it even was a requirement?  if it doesn't exist in SCM, it doesn't exist.

---

![fit] (images/deprecated.png)

^Matt - Deprecated functions means version numbers are critical.  Image courtesy: http://blog.simpsn.com/replacing-deprecated-functions-in-phpthumb-to-be-compatible-with-php-version-5-3-0

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

# \#4: Backing Services

* Anything your application uses as a resource (database, queueing system, email, cache) should be referenced with 'bindings' to these services.
* All applications deployed with explicit references to data services in manifest.yml (mechanism for User Provided Services)
* Possibly discovered via:
  * Spring Cloud (pay attention to configuration files)
  * Discovery mechanism (Zookeeper, etcd, Consul etc )
  * Environment

Importance: High. Its easy to do, and follows with the Config rules above

^Rags

---

# \#5: Build Release Run

* Build, Release and Run are separate stages for the application life cycle.
* Use profiles (ala Spring Boot) for running in different environments. Profiles should be easily grepable.

> The process of turning the code into a bundle of scripts, assets and binaries that run the code is the build. The release sends that code to a server in a fresh package together with the nicely-separated config files for that environment (see Config again). Then the code is run so the application is available on those servers.

^Rags

---

# \#6: Processes

* As a rule, you want each of those instances of running code to be stateless.
* Seperation of concerns - each microservice is a single process
* This makes your app more resilient, and easier to recover

Importances: High. Makes tools like CF even possible

^Rags

---

# \#7: Port Binding

* Your app should not assume its the only thing running on the same port
* Bind an internal port/IP to external URL using load balancer

Importances: Moderate. Most tools like Heroku, CF do this for you, and enforce it

^Rags

---

# \#8: Concurrency

* An extension of 6 above.
* Not necessarily required for certain aspects (single process workers, etc)

Importances: Low. But it helps scale certain parts.

^Rags

---

# \#9: Disposability

* Losing a process should be a non event
* No loss of state for user if we lose a process
* Startup times should be low

Importances: Moderate. Makes it easy to release quickly

^Rags

---

# \#10: Dev / Prod Parity

* Dev MUST == Production in config, but not performance
* Following the above helps do this

---

![fit] (images/worksonmymachine.png)

---

![fit] (images/workedonmine.jpg)

---

# \#11: Logs

* Log *everything*
  * Storage is cheap
  * Searching is cheap
* Logs help fix problems *after* they happen
* Use tokens for specific flows

---

![fit] (images/criticalerror.png)

---

![fit] (images/rca.jpg)

---

# \#12: Admin Processes

* Use your app/framework for these... build in the tools as needed.
* Don’t run updates directly against a database
* Don’t run them from a local terminal window
* ChatOps can help here

Importances: Moderate. Helps prevent mistakes
