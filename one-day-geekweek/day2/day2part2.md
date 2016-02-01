# Cloud Foundry

---

A Cloud Native Platform for people who want to get stuff done.

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

* Deploy VM (the easy part - handled by IaaS...CMDB?)
* Secure VM (or write some puppet)
* Install runtime (with what?  rpm?  tarball?)
* install dependencies (or write some scripts)
* Install application (tarball? RPM? git?)
* Start application (how?  job engine?  keep it running?)
* Modify load balancer (how?)
* Modify firewall (how?)
* Add health checks (to where?  http? tcp? )

---

# Components:
 * Router
 * UAA
 * Cloud Controller / Health Manager
 * Elastic Runtime / Diego
 * Blob Store
 * Services
 * Doppler / Loggregator
 
---
 
![](https://github.com/cloudfoundry/docs-cloudfoundry-concepts/blob/master/images/diego/diego-overview.png?raw=true)
 
---

#Let's Try It 

(you have cf cli installed, right)?

---

* Clone this repo: `git clone https://github.com/mcowger/hello-python.git`
* Login to `cf`: `cf login`
  * target `api.run.pivotal.io`
  * This is Pivotal Web Services
* Move into the directory:
  * `cd hello-python`
  * `cd version2`
  * `cf push`
  
---

# Things that just happened:

* Deploy Container
* Install runtime 
* install dependencies 
* Install application 
* Start application 
* Modify load balancer 
* Modify firewall 
* Add health checks 