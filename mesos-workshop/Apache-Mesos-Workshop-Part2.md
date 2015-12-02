# Apache Mesos Workshop Part 2

![inline](https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Apache-Mesos-logo.jpg/220px-Apache-Mesos-logo.jpg)

---

## Agenda

1. How does Mesos compare to other schedulers?
2. Mesos vs "opinionated" PAAS, such as Cloud Foundry
3. The use case for running Mesos in a cloud such as Amazon AWS
4. Where to learn more
5. What are some current limitations of Mesos?
6. Q&A

---

## Schedulers

1. Mesos
2. Kubernetes
3. Swarm
4. Others (Fleet=CoreOS, Diego=CF, Magnum=OS)

---

## Kubernetes

- uses Docker containers to assemble *pods*
    - pods are smallest management unit and containers have "plumbing" to interoperate (e.g. micro-service per container)
- in contrast Mesos can manage containers AND non-containerized workloads (including Kubernetes)
- 
---

## Swarm

- Native clustering tool from Docker
- Uses standard Docker API
- Each host in cluster runs a Swarm agent
- One host runs a Swarm *manager*

---

## Schedulers compared

Mesos is most mature

- in use for years vs. months
- at scales that are orders of magnitude higher

    - 10,000+ nodes
    - deploy 50,000 containers in < 100 seconds

---


# IAAS vs PAAS

Mesos is best classified as a PAAS stack.

Like any PAAS, the abstraction layer inherently makes some choices for you. Freedom from complexity has a cost.

![inline](http://ih.constantcontact.com/fs087/1108762609255/img/2155.jpg)

---

# PAAS stacks are not alike

A variety of PAAS stacks exist that attempt to give you “everything you need” to create an app on Amazon, or your own hardware, provided you accept the constraints imposed by the platform. 

But marketing people hate to call these constraints. Instead, the PaaS stack is described as **opinionated**.

Some PAAS stacks are more opinionated than others

IAAS -> Mesos -> Kubernetes -> CloudFoundry

---

## Why run a PAAS in a cloud such as Amazon AWS

[http://virtualgeek.typepad.com/virtual_geek/2015/10/a-blunt-completely-unprofessional-and-very-accurate-analogy-about-cloud-foundry.html](http://virtualgeek.typepad.com/virtual_geek/2015/10/a-blunt-completely-unprofessional-and-very-accurate-analogy-about-cloud-foundry.html)

Building an app directly to a public cloud’s APIs or data models is analogous to having loads of unprotected sex. 

If you build an app that writes to any given cloud’s APIs or data structures (regardless of how “standard” you think those may be) that - you will have an unintended, accidental Cloud Native App baby. 



---

# Where to learn more

[https://open.mesosphere.com/](https://open.mesosphere.com/)

[https://open.mesosphere.com/advanced-course/](https://open.mesosphere.com/advanced-course/)

![inline](https://d255esdrn735hr.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/8762OS_Apache%20Mesos%20Essentials.jpg)

---

# Bonus material

Can skip to Q&A here if out of time in live presentation

---

# Mesos Limitation: Global Resource management

Mesos currently collects available resources from cluster agent nodes.

Some datacenter resource are datacenter wide, and are not really associated with any particular cluster node

examples:
- IP addresses
- VLANs or subnets
- Shared network addressable storage

Addressing this is a current Mesos roadmap focus

---

## Mesos Limitation: Persistent Storage for Mesos

Certain classes of applications, such as databases, require long term access to persistent storage. 

---

## Running State-ful applications 

Techniques are available to run these types of workloads on Mesos, but sometimes the methods involved are essentially work-arounds that amount to using storage *not managed* by Mesos

---

### Workaround: Use direct attached storage

- Locks your workload to a single cluster node after first run, defeating an essential benefit of a cluster scheduler - the dynamic assignment of workloads to any, or the most appropriate, cluster node

---

### Workaround: Use external storage such as NFS from within the application

- Mesos is oblivious to this use of storage and cannot deliver in its role as a data center OS, offering centralized management and audit
    - This violates a key best practice premise of 12 factor apps by requiring maintenance of run time platform configuration inside the app itself

---

### Better solution

- Use the new DVDI Isolator

---

## What is the DVDI Isolator Module

Mesos has a rich facility to support plugins that add features.

The DVDI Isolator is a *module*, which is a binary plugin for Mesos.

In particular, it is an *isolator* module, which is a module that runs on agent cluster nodes and can interact with resource usage

---

## Features of the Mesos DVDI Isolator

- Manages external storage - storage that is network attachable to multiple cluster nodes,  
- Allows an application workload to be configured with a declarative statement describing its storage needs
    - This declaration is managed by Mesos. For example it can be done using the Marathon API.

---

##  Manages full volume mount lifecycle

- Allows a volume to be composed or allocated  and formatted from a pool upon first task run.
- Allows subsequent task runs to re-attach to the volume, even if the task runs on a different cluster node each time

---

## Supports Many storage types

- AWS EC2 EBS
- EMC ScaleIO
- EMC ExtremeIO
- many others too including NFS

Some of these storage types allow declarative specification of a rich set of storage attributes such as IOPs 

---

## The DVDI Storage Interface

DVDI stand for Docker Volume Driver Interface.

It leverages the internal storage volume interface of Docker.

-  The rapid investment growth in Docker related infrastructure is resulting in widespread implementation of the Docker interface by all popular forms of storage

--- 

## Why wasn't Docker sufficient by itself

- The DVDI Isolator allow a Mesos workload to take advantage of any storage with a Docker interface *but does not require that application to run in a Docker container*
- Many Mesos workloads do not run in Docker containers

---

## DVDI Isolator Architecture

![inline](https://emccode.files.wordpress.com/2015/10/screen-shot-2015-10-06-at-7-03-01-pm.png?w=521&h=379)

---

## Production grade Mesos installation

- Mesos requires a minimum of 3 Masters for HA. 5 are recommended to let you take one out of service (planned maintenance) and still tolerate a node failure. Adding masters requires a cluster restart.
- 5 (or more) Zookeeper nodes are recommended
- ZK and Master nodes can be co-located (commonly done) 
    - an even number of ZK nodes is supported, but not recommended because incrementing to even does not increase fault tolerance. Even number of Masters not recommended.

---

## Co-locating Mesos Master and Agent

- On a small cluster (< 10 nodes), Master and Agent could be colocated, but *never on a large cluster* (> 100 nodes)
    - On a small cluster, the active Master uses a small amount of CPU, memory and network. (Standby masters obviously use even less)

---

## Network traffic

- Once a cluster gets large (>100 nodes) Master network traffic is significant
- Framework schedulers (e.g. Spark, Marathon, Chronos) really only need connectivity to Master and Zookeeper nodes since all communication to agent nodes goes through a Master.
    - exception: if you use a meta-framework like Marathon to run another scheduler, it will of course be running on an agent node

---

# Q&A


deck available at [https://github.com/emccode/training](https://github.com/emccode/training)

follow speaker on twitter: @cantbewong

EMC{code}: [http://emccode.github.io/](http://emccode.github.io/)