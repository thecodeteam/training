# [fit] DevOps Agile Geek Week
## Day 3

^ Open this presentation with [Deckset](http://www.decksetapp.com/)
^ Matt

---

#Today's Focus:

# [fit] Cloud Foundry & Related Services

---

# [fit] Part 1: What's a PaaS?

---

PaaS is a category of cloud computing services that provides a platform allowing customers to develop, run and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.

---


# CF 101

>what problems does it solve?

* managing operating systems sucks.
* managing runtimes sucks
* managing deployment of dependencies sucks
* managing application isolation sucks
* managing deployment tasks sucks

---


## Process for deploying/scaling app on EC2 / EHC / etc

1. Deploy VM (the easy part - handled by IaaS...CMDB?)
2. Secure VM (or write some puppet)
2. Install runtime (with what?  rpm?  tarball?)
3. install dependencies (or write some scripts)
4. Install application (tarball? RPM? git?)
5. Start application (how?  job engine?  keep it running?)
6. Modify load balancer (how?)
7. Modify firewall (how?)
8. Add health checks (to where?  http? tcp? )

---

## Process for deploying app on CF

1. `cf push app_name`

## Process for scaling app on CF

1. `cf scale app_name -i instance_count`

---

# [fit] Components

---

* Cloud Controller

* UAA

* Diego

* Loggregator

* GoRouter

* Buildpacks

* Services

* BOSH

---

# Cloud Controller

* API layer

* `cf` cli talks to this

```
mcowger@hex:~
$ cf apps
Getting apps in org EVP / space EMC as matt.cowger@emc.com...
OK

name                    requested state   instances   memory   disk   urls
boisecode               stopped           0/1         128M     1G     boisecode.cfapps.io
bourbonTweetAlerts      started           1/1         256M     1G     bourbontweetalerts.cfapps.io
cfworker                started           1/1         128M     1G     cfworker.cfapps.io
```

---

# UAA

* Authentication layer

* Internal or LDAP Backend

* OAUTH2 Provider

* Recent EMC work

---


# Diego

* Elastic Runtime Components

  * Container Management (through Garden)
  * Container Scheduling
  * Droplet Creation
  * Placement / Availability Management
  * Deployment of Applications

* Recent rewrite to enable new hotness

---

# Loggregator

* Platform for delivering application log output

* Collates as needed

* `Firehose` too


##Example

```
$ cf logs --recent chargers2
2015-06-02T08:45:42.48-0700 [App/0]      OUT chargers2.cfapps.io - [02/06/2015:15:45:42 +0000] "GET / HTTP/1.1" 200 0 8461 ...
2015-06-02T08:45:45.06-0700 [App/1]      OUT chargers2.cfapps.io - [02/06/2015:15:45:45 +0000] "GET / HTTP/1.1" 200 0 8461 ...

```


---

# Gorouter


* Accepts requests for a specific 'route' (URL)

* Passes them to available applications & instances assigned to that route (possibly more than 1)

* Can be replaced by other load balancers if needed

---

# Buildpacks

* Provide basis for running application:

  * Language runtime (`Ruby`, `Python`, `COBOL`, `Java`, etc)
  * Module installation (as needed)
  * Debugger setup (as needed)
  * anything language or environment specific

---

# Services

> no application is an island

* External tools automatically provisioned & attached

  * Databases (MySQL, Oracle, Postgres)
  * NoSQL (Redis, MongoDB, etc)
  * Message Queues (0mq, RabbitMQ, etc)


---

# BOSH

* Responsible for using the IaaS (vSphere, vCD, OpenStack, AWS, etc) to build virtual machines

* VMs are called 'cells'

  * CF on Bare Metal is coming :)
  * Currently based on Ubuntu
  * Support for VMware Photon is planned

---


# BOSH, cont.

* Responsible for managing:

  * Long Running Processes (services, apps, parts of itself)
  * Tasks (single run requests (deploy X, create Y))
  * Upgrades of infrastructure


---

# Demo


---


# [fit] cf push



---



# [fit] now you!

```
git clone https://github.com/mcowger/hello-python.git
cd hello-python
cf login
cf push hello-<yourname>
...
http://hello-yourname.cfapps.io

```
