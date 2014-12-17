# Docker management overview

### Jonas Rosland
### Developer Advocate
#### @virtualswede
#### jonas.rosland@emc.com
#### emccode.github.io
#### December 2014

^ Run this presentation with [Deckset](http://www.decksetapp.com/)

---

Different types of management

**Developer-focused:**
- Fig
- Panamax

**Ops-focused:**
- Kubernetes
- Mesos
- Fleet
- Docker Swarm

---

# Fig

---

## Fig

Fast, isolated development environments using Docker.
Orchard acquired by Docker July 2014
Docker's first acquisition

![inline](http://www.fig.sh/img/logo.png)

---

## Fig example (1/3)

Let's define two services:

**web**
- built from Dockerfile
- run the command python app.py inside the image
- forward the exposed port 5000 on the container to port 5000 on the host machine
- connect to the Redis service
- mount the current directory inside the container

**redis**, which uses the public image redis

---

## Fig example (2/3)

Dockerfile:

```
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
```

---

## Fig example (3/3)

fig.yml:

```
web:
  build: .
  command: python app.py
  ports:
   - "5000:5000"
  volumes:
   - .:/code
  links:
   - redis
redis:
  image: redis
```
---

## Docker Compose is Fig Next Gen

```
containers:
  web:
    build: .
    command: python app.py
    ports:
    - "5000:5000"
    volumes:
    - .:/code
    links:
    - redis
    environment:
    - PYTHONUNBUFFERED=1
  redis:
    image: redis:latest
    command: redis-server --appendonly yes
```

---

# Panamax

---

## Panamax

An open-source project that makes deploying complex containerized apps as easy as Drag-and-Drop
Created by CenturyLink Labs
Released in August 2014

![inline, white](https://camo.githubusercontent.com/257d9eef6494599b12eb31e8221ce7fd97b13593/687474703a2f2f70616e616d61782e63612e74696572332e696f2f70616e616d61785f75695f77696b695f73637265656e732f70616e616d61785f6c6f676f2d7469746c652e706e67)

---

![inline](http://virtualswede.files.wordpress.com/2014/08/screen-shot-2014-08-12-at-2-18-04-pm.png)

---

## Search for images

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-7-52-58-pm.png)

---

## Run images in "apps"

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-7-53-12-pm.png)

---

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-7-54-47-pm.png)

---

## Manage and add more images to an app

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-8-04-44-pm.png)

---

## Expose ports

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-8-09-28-pm.png)

---

## Link containers together

![inline](https://virtualswede.files.wordpress.com/2014/09/screen-shot-2014-09-08-at-8-20-00-pm.png)

---

# Kubernetes

---

## Kubernetes

An open source system for managing containerized applications across multiple hosts

Providing basic mechanisms for deployment, maintenance, and scaling of applications

---

## Kubernetes main features

- lean: lightweight, simple, accessible
- portable: public, private, hybrid, multi cloud
- extensible: modular, pluggable, hookable, composable
- self-healing: auto-placement, auto-restart, auto-replication

---

## Kubernetes concepts (1/2)

**Clusters** are the compute resources on top of which your containers are built

**Pods** are a colocated group of Docker containers with shared volumes - smallest deployable units that can be created, scheduled, and managed with Kubernetes

---

## Kubernetes concepts (2/2)

**Replication** controllers manage the lifecycle of pods, ensuring that a specified number of pods are running at any given time, by creating or killing pods as required

**Services** provide a single, stable name and address for a set of pods, acting as basic load balancers

**Labels** are used to organize and select groups of objects based on key:value pairs

---

![inline](http://kubernetes.io/img/desktop/graphs/graph-01.svg)

---

## Kubernetes pod example

```
{
  "id": "redis-master",
  "kind": "Pod",
  "apiVersion": "v1beta1",
  "desiredState": {
    "manifest": {
      "version": "v1beta1",
      "id": "redis-master",
      "containers": [{
        "name": "master",
        "image": "dockerfile/redis",
        "cpu": 100,
        "ports": [{
          "containerPort": 6379,
          "hostPort": 6379
        }]
      }]
    }
  },
  "labels": {
    "name": "redis-master"
  }
}
```

---

# Mesos

---

## Mesos

Abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual)

Enables fault-tolerant and elastic distributed systems to easily be built and run effectively

![inline](http://mesos.apache.org/assets/img/mesos_logo.png)

---

## Mesos functionality

The Mesos kernel runs on every machine and provides applications (e.g., Hadoop, Spark, Kafka, Elastic Search) with API’s for resource management and scheduling across entire datacenter and cloud environments

Also manages containers, of course

All using one API to provision and manage everything

---

## More on Mesos

I highly recommend reading up on Mesosphere

---

# Fin
