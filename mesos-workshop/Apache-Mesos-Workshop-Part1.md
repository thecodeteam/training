# Apache Mesos

![inline](https://upload.wikimedia.org/wikipedia/en/thumb/0/0d/Apache-Mesos-logo.jpg/220px-Apache-Mesos-logo.jpg)

---

## Agenda (part 1 45 minutes)

1. Who are the presenters?
2. What is Mesos?
3.  Why do I care? What will it do for me?
4. How do I run it? What is required?

---

## Agenda continued

- How stable is this thing? If I put this in production tomorrow, will I get called at 2AM and then get fired the next day?
- Description of logical Architecture
- Installation process described

(break) 

---

## Agenda - part 2
 - **Hands on workshop**, deploy a web application to a Mesos cluster
  - If time allows:
     - Comparison with other data center management technologies
     - Advanced topics and roadmap 
- Audience Q&A

---

## Who are the presenters?

Steve Wong Developer Advocate, EMC{code}

- currently an open source contributor, storage related enhancements for Mesos

deck available at [https://github.com/emccode/training](https://github.com/emccode/training)
 
---

## What is Apache Mesos?

From a resource perspective, it's a cluster manager:

- Pools Computers into a centrally managed resource pool managed as a unit

From an application perspective, it's a scheduler (=dispatcher)

- Dispatches workloads which consume the pooled resources

Often described as a Data Center Operating System (DCOS)

---

## Mesos as a Cluster Manager

When you assemble a cluster and use it, 
there is no getting around it, 
*you are building a distributed system*

- These are difficult to design, build and operate
- They introduce exponentially more complexity

Mesos is a tool that takes on some of the "heavy lifting" of deploying and operating a distributed system

---

![inline](http://image.slidesharecdn.com/mesosreport-03v1-140424214256-phpapp02/95/mesos-study-report-03v12-4-638.jpg?cb=1398375831)

---

# Assume manual workload placement.  What are the odds that every workload, will use exactly 100% of the CPU + memory + storage, on its machine, all the time

# **?**

---

## Summary: What will Mesos do for me?

1. Runs a wide assortment of workloads
2. On commodity hardware
3. With great efficiency
4. With high availability / fault tolerance
5. While offering both UI and API management interfaces 

---

# What does "supports a wide variety of workloads" really mean?

---

## Two levels of Application support

1. Generic: You can use this to run anything that can be launched in a standard Linux shell, including Docker containerized applications. **Marathon** (or Aurora)

2. **Framework** is a plug-in to Mesos that allows you to implement a *sub-scheduler*.

    - The framework extends Mesos to provide custom workload placement and resource allocation
        - for example, reserve 10% of the cluster's resources to Hadoop jobs, and  framework manages prioritized dispatch of individual Hadoop jobs.

---

## Marathon framework runs these types of applications

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/Mesos%20application%20support.png?raw=true)

---

## Mesos Frameworks

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/mesos%20frameworks.png?raw=true)

plus Kubernetes and others, 
and you can write your own

---

### Marathon

![](https://mesosphere.com/wp-content/themes/mesosphere/library/images/components/services/marathon.jpg)

-  Marathon acts as a service dispatcher - you provide instructions and Marathon does its best to keep the service up on the cluster providing automated scaling and high availability restarts
- If you choose to write your own framework, you can run it under Marathon to "save work related to"inherit" automated scaling and high availability

---

## Chronos is "chron" for a Mesos datacenter

![inline](https://mesosphere.com/wp-content/themes/mesosphere/library/images/assets/chronos-ui-serenity-theme.jpg)

---

## With Marathon and Chronos, Mesos manages on-demand jobs, scheduled jobs, long running services


![inline](https://emccode.files.wordpress.com/2015/08/mesos.png)  

---


## What does "runs on commodity hardware" mean?

- "bare metal" x86 hardware
- a VM 
    - running on your favorite hypervisor in your data center, OR
    - running in your favorite public cloud

---

## Mesos runs on all of these

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/Mesos%20Hosts.png?raw=true)

---

## Any cluster node limitations?
 
- They do not have to be identical in processor model, speed or size.
- They can concurrently run non-Mesos services - you don't have to give Mesos control over the whole node's CPU, memory or disk.
- Elastic scaling is supported
    - nodes can come and go.

---

## How stable is Mesos
 
  ![](http://www.google.com/about/careers/files/story_a-rare-inside-look-at-google-data-centers_image_726x726.jpg)
  
 1. Has has been in production use,
 2.  at 10,000 node scales,
 3.  by recognized  users,
 4.  for over 2 years
 
---

## Powered by Mesos

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/Mesos-Users.png?raw=true)

---
 
## Started at UC Berkeley in 2009, became an Apache project in 2013 after nearly two years in incubation

see [WIred: How Twitter rebuilt Google's Borg March 2013](http://
www.wired.com/2013/03/google-borg-twitter-mesos/)

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/wired%20mesos%20screenshot.png?raw=true)


![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/mesos%20paper%20screenshot.png?raw=true)

---

## Goal: Abstract distributed system complexities

- Fault tolerance, with leader election
- sending workloads out to distributed nodes for execution
- handling failures in distributed executors
    - including detecting sick tasks, terminating them and restarting workloads

Frameworks do not have to deal with these things, and can focus on the "business logic" of the application they manage
 
---
 
## Performance characteristics
 
linear scalability characteristics - (circa 2010)

![inline](http://www.nextplatform.com/wp-content/uploads/2015/09/mesos-scale.jpg)

---
 
## More recent performance metric

50,000 containers deployed live on stage in 1 minute 12 seconds

![inline](https://mesosphere.com/wp-content/uploads/2015/10/image01-800x602@2x.png)
 
 ---
 
## How do I run Mesos in production?
 
- 3 nodes running Zookeeper and Mesos Master
- Agent nodes


A dev, learning, non-production system can be built on a single host. 
 
 ---
 
## Overview of service components

![inline](https://github.com/emccode/training/blob/master/mesos-workshop/images/mesos%20overview.png?raw=true)
 
 ---
 
## Mesos task dispatch workflow
 
![inline](http://image.slidesharecdn.com/mesospherewebcast-140805130801-phpapp02/95/apache-mesos-and-mesosphere-live-webcast-by-ceo-and-cofounder-florian-leibert-31-638.jpg?cb=1442180394)

---

## Mesos Installation

The advanced online course is highly recommended

[http://open.mesosphere.com/advanced-course/](http://open.mesosphere.com/advanced-course/)

In the interest of time, the hands on portion of this workshop will continue with a Mesos cluster that is pre-deployed in the Amazon cloud, in a way similar to the Mesosphere course...

---

## Demo
 