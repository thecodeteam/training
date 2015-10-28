Lab V: Networking Between Container Hosts
===============================

## Description

In this lab, you'll learn how to have containers talk to each other using overlay networks.

### Lab setup

Each participant has been handed a piece of paper with two machines `student00Xa` and `student00Xb` with their associated IP addresses. Each machine has been provisioned by Docker Machine with Docker 1.9 and REX-Ray 0.2 installed for use. The SSH password for each host is the host name. ie. Host `student001a`'s password is `student001a` 

**NOTE:** `v1.0.0-rc1` is going to be used for Swarm as of this writing to allow libnetwork to properly function.

#### Mac/Linux
Use Terminal
`ssh IPADDRESS -l student001a`

#### Windows
Use PuTTy


## Destroy the existing Swarm instance
Networking in Docker 1.9 requires the use of Consul as the swarm dependency. So we are going to create a new Swarm instance for our hosts.

Get back to default and point the CLI to the local docker instance.
```
$ unset DOCKER_TLS_VERIFY
$ unset DOCKER_HOST
```

Stop and remove the Swarm Agents on both hosts `a` and `b`.
```
$ docker stop swarm-agent
$ docker rm swarm-agent
```

On host `a`, remove the Swarm Master
```
$ docker stop swarm-agent-master
$ docker rm swarm-agent-master
```

## Create A New Swarm Instance with Consul
Next, we need to add a few Docker Engine options which are necessary for networking to function. Perform these functions on both hosts `a` and `b`:
```
$ sudo service docker stop
$ sudo sed -i '10 a --cluster-advertise='$(curl http://169.254.169.254/latest/meta-data/public-ipv4)':2376' /etc/default/docker
$ sudo sed -i '10 a --cluster-store=consul://CONSULIP:8500' /etc/default/docker
$ sudo service docker start
```

On host `a` start a consul server:
```
$ docker run -d -p 8500:8500 -h consul progrium/consul -server -bootstrap-expect 1
```

Now we can configure our new Swarm agents on each host `a` and `b`:
```
$ docker run -d --restart=always --name swarm-agent-consul swarm:1.0.0-rc1 join --advertise $(curl http://169.254.169.254/latest/meta-data/public-ipv4):2376 consul://<hostaIP>:8500
```

Start swarm manager on `a`
```
$ docker run -d --restart=always --name swarm-agent-master-consul -p 3376:3376 -v /etc/docker:/etc/docker swarm:1.0.0-rc1 manage --tlsverify --tlscacert=/etc/docker/ca.pem --tlscert=/etc/docker/server.pem --tlskey=/etc/docker/server-key.pem -H tcp://0.0.0.0:3376 --strategy spread consul://<hostaIP>:8500
```

On Host `a` point the Docker CLI to the new Swarm instance:
```
$ export DOCKER_TLS_VERIFY=1
$ export DOCKER_HOST=tcp://$(curl http://169.254.169.254/latest/meta-data/public-ipv4):3376
```

Performing a `docker info` should give you a Swarm output:
```
student001a@student001a:~$ docker info
Containers: 4
Images: 4
Role: primary
Strategy: spread
Filters: affinity, health, constraint, port, dependency
Nodes: 2
 student001a: 52.91.204.239:2376
  └ Containers: 2
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.017 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=3.19.0-30-generic, operatingsystem=Ubuntu 14.04.3 LTS, provider=amazonec2, storagedriver=aufs
 student001b: 54.86.251.223:2376
  └ Containers: 2
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.017 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=3.19.0-30-generic, operatingsystem=Ubuntu 14.04.3 LTS, provider=amazonec2, storagedriver=aufs
CPUs: 2
Total Memory: 2.033 GiB
Name: 33b92fe60f6e
```

## Network the Containers
Create a new overlay network which containers can join. `multihost` is an arbitrary name and can be called whatever you want:
```
docker network create -d overlay multihost
```

Create our first container and using a constraint, pin it to host `a`. This will leave a host idle with `top` running.
```
docker run -d --name="long-running" --net="multihost" --env="constraint:node==*a*" busybox top
```

Pin the second container to host `b` and ping `long-running` container:
```
docker run -it --rm --net="multihost" --env="constraint:node==*b*" busybox ping long-running
```


## Congratulations!!

You've configured two containers on different hosts to talk to each other using overlay networking!