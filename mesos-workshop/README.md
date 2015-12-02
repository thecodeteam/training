Mesos Workshop
================

### Mesos Introduction

A 2 hour workshop that takes the attendees from "What is Mesos" to a hands-on deployment of a web server on a Mesos cluster.

Covers:

- What is Mesos? and What can it do for me?
- What kinds of workloads can it support?
- How large can it scale, and how does its performance hold up at scale?
- How would I go about deploying it?
- How does Mesos compare to other schedulers / cluster managers?
- Mesos features and roadmap related to external and persistent storage

---

### Presentation flow:

1. Present deck #1(35-45 minutes)
2. Hands-on lab (20-30 minutes)
    - Attendees utilize the Marathon UI to deploy a web server, so they can use a laptop, tablet , or smartphone that can connect to AWS hosts.
3. Wrapup with Deck #2
4. Q&A

---

### Pre-configured lab setup

The hands-on lab portion of this workshop anticipates a preconfigured Mesos cluster in AWS - though nothing inherently precludes running in another cloud or on "bare metal".  

A workshop for 30 attendees can be done with 9 AWS instances, deployed as follows.

1. t2.micro running
    - Ubuntu 14.04
    - Mesos Master
    - Zookeeper
2. t2.micro running
    - Ubuntu 14.04
    - Mesos Master
    - Zookeeper
    - Marathon
3. t2.micro running
    - Ubuntu 14.04
    - Mesos Master
    - Zookeeper
    - Chronos
4. 6 instances of t2.micro running
    - Ubuntu 14.04
    - Mesos Slave
    - Python, Golang installed
    - Docker installed (optional)
    - RexRay and DVDCLI installed (optional)
5. AWS security group with ports open on
    - 22 (ssh)
    - 4400 (Chronos)
    - 5050 (Mesos Master)
    - 8080 (Marathon)
    - 31000-32000 (ephemeral ports for attendee web servers)