# DevOps Agile Geek Week
## Day 3

^ Open this presentation with [Deckset](http://www.decksetapp.com/)
^ Matt

---

#Today's Focus: Cloud Foundry & Related Services

---

# Part 1: What's a PaaS?

---

PaaS is a category of cloud computing services that provides a platform allowing customers to develop, run and manage Web applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.


---

## Process for deploying app on EC2 / EHC / etc

1. Deploy VM
2. Secure VM
2. Install runtime
3. install dependencies
4. Install application
5. Start application
6. Modify load balancer
7. Modify firewall
8. Add health checks

---

## Process for deploying app on CF

1. `cf push app_name`

---

## Process for scaling app on EC2 / EHC/ etc

1. Deploy VM
2. Secure VM
2. Install runtime
3. install dependencies
4. Install application
5. Start application
6. Modify load balancer
7. Modify firewall
8. Add health checks

---

## Process for scaling app on CF

1. `cf scale app_name -i instance_count`

---

# CF 101

>stuff a developer usually doesn't need

---

##Components in CF

* BOSH
* CloudController
* Blobstore / Droplets
* NATS
* HealthManager (HM9K)
* DEA
* Warden

---

## BOSH / Stemcell

* Deployment
* Process Mgmt
* Task Mgmt
* Stemcell?
---

## CloudController

* API endpoint
* 'stack' configuration

---

## Blobstore

* Cache of droplets
* Droplets

---

## NATS

* Messages Bus for communication between components

---

## Health Manager

* collect the desired state of the world (from the CC via HTTP)
* collect the actual state (from the DEAs via application heartbeats over NATS)
* perform a set diff to find discrepancies – e.g. missing apps or extra (rogue) apps
* send START and STOP messages to resolve these discrepancies

---

## DEA

* Droplet Execution Agent
* Control execution of containers/instances

---

## Warden

* container technology used (being replaced)
* consumes droplets from blobstore
* executed by DEA

---

# Demo
