# Docker Workshop

A full-day workshop that gives you enough information to start planning to run Docker containers in your own organization.

The workshop is intended for Docker beginners, so if you're wondering which orchestration tool you should implement or worried about how to run large-scale L2 networks this is NOT the event for you.

So, if you're new to Docker and looking for a great introduction, this will is a great opportunity to get a hands-on introduction to the fundamentals.


**Prerequisites:**

Use your own laptop with The Docker Toolbox (https://www.docker.com/toolbox) installed.

### Agenda:

#### Part I: Introduction to Docker
 - Overview, 1h, [presentation here](http://www.slideshare.net/jonasrosland/docker-and-containers-overview-docker-workshop)
 - Docker ecosystem, 20 min
  - Network
  - Storage
  - Management

#### Lab I: Run your first container

 - Start it
 - See the logs
 - See which ports are open
 - Connect to the container

#### Lab II: Building containers with Dockerfiles

 - Write your first Dockerfile
 - Build your first container
 - Run it and repeat the previous lab

#### Part II: Docker in Production

This section explores the issues in running Docker in a production environment, which is exactly what you'll want to do after the training is over :)

 - Introduction to clustering
 - CoreOS
 - Docker Machine and Swarm
 - Starting a cluster
 - Resource scheduling
 - Service discovery (etcd, Consul, Zookeeper, etc)
 - High availability
