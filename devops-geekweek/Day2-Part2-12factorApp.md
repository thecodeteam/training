# The 12 factor App

^ Open this presentation with [Deckset](http://www.decksetapp.com/)
^ Matt

---

### The Basics

* This was in your home work :)

> much of this source: http://www.clearlytech.com/2014/01/04/12-factor-apps-plain-english/

---

# \#1: Codebase

* One codebase tracked in revision control, many deploys
* Put all your code in a source control system. Heck, just put it up on GitHub from the start.

Importance: Non-negotiable. Everyone does this, and developers will laugh at you if you aren’t.

---

# \#2: Dependencies

* Dependencies must be explicitly declared
* They should be declared with the rest of the code, and tracked the same way
* Dependencies tracking should contain version numbers of dependencies

Importance: High. Without this, your team will have a constant slow time-suck of confusion and frustration, multiplied by their size and number of applications. Spare yourself.

---

# \#3: Config

* Config belongs in the environment if possible - it varies between deploys, but the code doesn't
* Includes access credentials, logging config, etc.
* Should be read at runtime, not preprocessed into code.

Importance: Medium. You can get away without it, but its sloppy.

---

# \#4: Backing Services

* Anything your application uses as a resource (database, queueing system, email, cache) should be referenced with 'bindings' to these services.
* Possibly discovered via:
  * Discovery mechanism (Zookeeper, etcd, Consul etc )
  * Environment

Importance: High. Its easy to do, and follows with the Config rules above

---

# \#5: Build Release Run

* Build, Release and Run are separate stages for the application life cycle.

> The process of turning the code into a bundle of scripts, assets and binaries that run the code is the build. The release sends that code to a server in a fresh package together with the nicely-separate config files for that environment (see Config again). Then the code is run so the application is available on those servers.

---

# \#6: Processes

* As a rule, you want each of those instances of running code to be stateless.
* This makes your app more resilient, and easier to recover

Importances: High. Makes tools like CF even possible

---

# \#7: Port Binding

* Your app should not assume its the only thing running on the same port
* Bind an internal port/IP to external URL using load balancer

Importances: Moderate. Most tools like Heroku, CF do this for you, and enforce it

---

# \#8: Concurrency

* An extension of 6 above.
* Not necessarily required for certain aspects (single process workers, etc)

Importances: Low. But it helps scale certain parts.

---

# \#9: Disposability

* Losing a process should be a non event
* No loss of state for user if we lose a process
* Startup times should be low

Importances: Moderate. Makes it easy to release quickly


---

# \#10: Dev / Prod Parity

* Dev MUST == Production in config, but not performance
* Following the above helps do this

Importances: Critical. You can't do continuous push (or push at all) safely without it.

---

# \#11: Logs

* Log *everything*
  * Storage is cheap
  * Searching is cheap
* Logs help fix problems *after* they happen
* Use tokens for specific flows

Importances: High. Can't debug without logs.

---


# \#12: Admin Processes

* Use your app/framework for these... build in the tools as needed.
* Don’t run updates directly against a database
* Don’t run them from a local terminal window
* ChatOps can help here

Importances: Moderate. Helps prevent mistakes
