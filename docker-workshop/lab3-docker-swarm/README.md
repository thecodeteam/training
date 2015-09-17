Create a cluster of container hosts
===============================

# Description

In this lab you'll use Docker Machine to set up a "swarm" of container hosts, a cluster that you can manage and schedule containers on top of.

## The Docker Swarm master

We need a Swarm Master that will be our main point of contact for the entire cluster.
First we need to create a discovery token, and we can use our existing container host to create one for us:

```
$ docker run swarm create
<snip>
Status: Downloaded newer image for swarm:latest
8d7dc77346a4e0d999fd38cc29ed0d38
```

The last line is our discovery token that is ours and ours alone, and we will take that token and create our Swarm Master with it:

```
$ docker-machine create -d virtualbox --swarm --swarm-master --swarm-discovery token://YOURTOKENHERE swarm-master
426583efc6a swarm-master
Creating VirtualBox VM...
Creating SSH key...
Starting VirtualBox VM...
Starting VM...
To see how to connect Docker to this machine, run: docker-machine env swarm-master
```

We are actually using a public discovery service, so you can head over to `https://discovery.hub.docker.com/v1/clusters/YOURTOKENHERE` and see the IP address of your Swarm Master. You'll see more nodes coming up in a just a few minutes.

But first, let's make sure your environment variable are correct by running the following command:

`eval $(docker-machine env --swarm swarm-master)`

Let's have a look at `docker info`:

```
$ docker info
Containers: 2
Images: 1
Role: primary
Strategy: spread
Filters: affinity, health, constraint, port, dependency
Nodes: 1
 swarm-master: 192.168.99.100:2376
  └ Containers: 2
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.022 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=4.0.9-boot2docker, operatingsystem=Boot2Docker 1.8.2 (TCL 6.4); master : aba6192 - Thu Sep 10 20:58:17 UTC 2015, provider=virtualbox, storagedriver=aufs
CPUs: 1
Total Memory: 1.022 GiB
Name: 7bd1a650694a
```

You can se we have just one node in our cluster (the Swarm Master), we have 1 CPU and 1GB or memor we can use. Let's add some more resources!

## Create Docker Swarm Nodes

We will now create the nodes of our Docker Swarm so we actually have a cluster and not just a single container host.

Run the following command to create your first and second node:

```
$ docker-machine create -d virtualbox --swarm --swarm-discovery token://YOURTOKENHERE swarm-node1
$ docker-machine create -d virtualbox --swarm --swarm-discovery token://YOURTOKENHERE swarm-node2
```

Now let's run `docker info` again:

```
$ docker info
Containers: 4
Images: 3
Role: primary
Strategy: spread
Filters: affinity, health, constraint, port, dependency
Nodes: 3
 swarm-master: 192.168.99.100:2376
  └ Containers: 2
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.022 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=4.0.9-boot2docker, operatingsystem=Boot2Docker 1.8.2 (TCL 6.4); master : aba6192 - Thu Sep 10 20:58:17 UTC 2015, provider=virtualbox, storagedriver=aufs
 swarm-node1: 192.168.99.101:2376
  └ Containers: 1
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.022 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=4.0.9-boot2docker, operatingsystem=Boot2Docker 1.8.2 (TCL 6.4); master : aba6192 - Thu Sep 10 20:58:17 UTC 2015, provider=virtualbox, storagedriver=aufs
 swarm-node2: 192.168.99.102:2376
  └ Containers: 1
  └ Reserved CPUs: 0 / 1
  └ Reserved Memory: 0 B / 1.022 GiB
  └ Labels: executiondriver=native-0.2, kernelversion=4.0.9-boot2docker, operatingsystem=Boot2Docker 1.8.2 (TCL 6.4); master : aba6192 - Thu Sep 10 20:58:17 UTC 2015, provider=virtualbox, storagedriver=aufs
CPUs: 3
Total Memory: 3.065 GiB
Name: 7bd1a650694a
```

Now you can see that we have 3 nodes, totalling 3 CPUs and 3GB of memory that we can use for our containers, awesome! Also, revisit `https://discovery.hub.docker.com/v1/clusters/YOURTOKENHERE` to see that you now have the IP addresses and ports for all three hosts.

Now let's start a few containers and you'll see that are being scheduled on top of all three container hosts. When you do a `docker pull` or a `docker run`, it might seem like the process is hanging but just wait and it will eventually give you some output.

```
$ docker run -d redis
5ec99f019f00d763e7dde4c1d0315f44c92e5c66ce3f9e70454168d1a227b1ff
$ docker run -d nginx
8552e93bc2a02d683a342d9ba792f517b396d028b0cc6fb9aca2bd7d87fe06e7
$ docker run -d postgres
6abbe9cbebc7a19773e30db4537783460f153188a1b57d0d55c7cd3e61d1653f
```

Now if we look at where those containers are actually running we can see that they are on different hosts by the names they are given:

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
6abbe9cbebc7        postgres            "/docker-entrypoint.s"   41 seconds ago      Up 38 seconds       5432/tcp            swarm-master/goofy_einstein
8552e93bc2a0        nginx               "nginx -g 'daemon off"   2 minutes ago       Up 2 minutes        80/tcp, 443/tcp     swarm-node2/silly_bardeen
5ec99f019f00        redis               "/entrypoint.sh redis"   3 minutes ago       Up 3 minutes        6379/tcp            swarm-node1/distracted_turing
```

There you go, you now have a 3 node Docker Swarm cluster up and running on your laptop, with 3 containers scheduled across them, and using a public service discovery instance to manage your cluster.
