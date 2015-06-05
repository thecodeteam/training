# Docker Compose and Panamax

### Jonas Rosland
### Developer Advocate
#### @jonasrosland
#### jonas.rosland@emc.com
#### emccode.github.io
#### June 2015

^ Run this presentation with [Deckset](http://www.decksetapp.com/)

---

Different types of management

**Developer-focused:**
- Fig
- Panamax

**Ops-focused:**
- Kubernetes
- Mesos
- Tectonic
- Fleet
- Docker Swarm

---

# First a bit of history

---

# Fig

---

## Fig

Fast, isolated development environments using Docker.
Orchard acquired by Docker July 2014
Docker's first acquisition

![inline](http://www.fig.sh/img/logo.png)

---

# Docker Compose
# (Fig 2.0)

---

# First, let's verify your installs

1. boot2docker/docker
2. Docker Compose

---

# boot2docker

```
$ boot2docker init
$ boot2docker up
Waiting for VM and Docker daemon to start...
.............................ooooooooooooooooooooooooooooooooooooooo
Started.
```

---


## Docker Compose example (1/3)

Let's define two services:

**web**
- built from Dockerfile
- runs the command `python app.py` inside the image
- forwards the exposed port 5000 on the container to port 5000 on the host machine
- connects to the Redis service
- mounts the current directory inside the container

**redis**, which uses the public image redis

---

## Docker Compose example (2/3)

Dockerfile:

```
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
```

---

## Docker Compose example (3/3)

docker-compose.yml:

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

# Fin
