Lab II: Building containers with Dockerfiles
===============================

## Description

In this lab you'll learn how to use Dockerfiles.

### Lab setup

Each of you has been handed a piece of paper with a machine that has Docker and REX-Ray installed. SSH into your machine

#### Mac/Linux
Use Terminal
`$ ssh student@IPADDRESS`

#### Windows
Use PuTTy

## Build your own container

Building containers is easy, and we'll show how to by using a Dockerfile.

A Dockerfile is just a simple textfile with information about what to start from (a linux distro usually), what commands to run before it's complete (installing packages and changing configuration files for instance), what port to open and lastly what binary to run.

There are more settings of course, and we'd recommend you to read up on them at the[Dockerfile reference](https://docs.docker.com/reference/builder/).

An easy container to build is the Redis key-value store service. We will go through the steps in [building Redis](https://docs.docker.com/examples/running_redis_service/).

1. from the home directory `touch Dockerfile`
2. use `vi` or `nano` to edit `Dockerfile` like `vi Dockerfile`
3. insert the following:
```
FROM        ubuntu:14.04
RUN         apt-get update && apt-get install -y redis-server
EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
```
4. Build the container `docker build -t <your username>/redis .`
5. Look at the available images with `docker images`
5. Run the service with `docker run --name redis -d <your username>/redis`


