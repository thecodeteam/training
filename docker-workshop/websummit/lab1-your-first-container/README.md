Lab I: Run your first container (Quick Refresher)
===============================

## Description

In this lab you'll learn use Docker, how to search for Docker images on Docker hub, and how to run your images and connect to the applications inside them.

### Lab setup

Each participant has been handed a piece of paper with two machines `student00Xa` and `student00Xb` with their associated IP addresses. Each machine has been provisioned by Docker Machine with Docker 1.9 and REX-Ray 0.2 installed for use. The SSH password for each host is the host name. ie. Host `student001a`'s password is `student001a`

#### Mac/Linux
Use Terminal
`ssh IPADDRESS -l student002a`

#### Windows
Use PuTTy

## Using Docker
SSH into host `a` using the public IP address provided.

Now that you have a container host there are several things you can do. If you just run the command `docker` you'll get a list of all the commands you can issue.

First off we want to have a look at the Docker installation information, so run:

`docker info`

This should give you an output similar to this:

```
$ docker info
Containers: 0
Images: 0
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 0
 Dirperm1 Supported: false
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 3.13.0-65-generic
Operating System: Ubuntu 14.04.2 LTS
CPUs: 1
Total Memory: 992.5 MiB
Name: student003
ID: DLZJ:LWWG:7VM2:YPHW:F67R:GAR2:76WK:L35Q:SQM6:A442:2OSG:L2JI
WARNING: No swap limit support
Labels:
 provider=amazonec2
```

Here we can see how many images we have downloaded,  how many containers we have running, and more info like version of Docker etc.

The second command we'll look at is searching for images that we find interesting.

The [Docker hub](https://hub.docker.com) currently has approximately **75000** images available for everyone to use freely.

Try a search for Sensu, a [really cool monitoring solution](http://sensuapp.org):

`docker search sensu`

You should get a list of Docker images that have been published and shared by the community, like this:

```
$ docker search sensu
NAME                                  DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
hiroakis/docker-sensu-server                                                          6                    [OK]
steeef/sensu-centos                   Sensu server on CentOS 6.x Forked from htt...   1                    [OK]
sstarcher/sensu-docker                                                                0                    [OK]
```

Try some other searches, like for redis, apache, nginx, mysql, postgresql, you name it, try to see if there are Docker images out there. Make note though that currently there are only linux applications and services out there. If you find an application or service that's not on the Docker hub, perhaps you could create one and be the first!

Now let's try to download an image using the `docker pull` command:

`docker pull ubuntu`

You'll see that Docker starts downloading a Docker image, this specific one is a base Ubuntu image. We'll try other images with more applications later.

When download is complete, your "Hello World" with Docker command looks something like this:

`docker run ubuntu echo hello world`

You can run other commands or invoke a bash shell like this:

`docker run -i -t ubuntu /bin/bash`

You'll see that `-i` means we'll run this container interactively, and `-t` means we're attaching a pseudo-TTY to it (essentially attaching a terminal), then giving Docker the name of the image we want to run, and a command within that image.

This will start the container, giving it its own file system, networking etc. and start up a shell for us to rummage around inside the container.

Now that you're in your container, look around a bit and run some commands, like `ifconfig` and `ls /`. You can even install applications here, so try to run `apt-get update` and then `apt-get install apache2 -y`.

You now have apache running in the container!

To exit the container, there are two options. `CTRL-d` exits the shell and shuts down the container. If you want to keep the container running but detach from it, do `CTRL-p CTRL-q`. You can then re-attach to it by running `docker attach UNIQUEID`.

## Run some simple apps

We will run tomcat which a Java based application server. To do this we use the following command.

```$ docker run -d -p 8888:8080 tomcat:8.0```

The image will be downloaded if required and tomcat will be run in a *deamon* mode.

Now run the following command.

```$ docker ps```

Which will yield an output that looks something like below (Partial output).

```
STATUS              PORTS                    NAMES
Up 17 seconds       0.0.0.0:8888->8080/tcp   romantic_stallman
```
Notice that under the PORTS section the port 8888 of the localhost is forwarded to port 8080 of tomcat running in the container.

You can run your apps by pointing your browser to ```http://IPADDRESS:8888```

Read more about the [docker run](https://docs.docker.com/reference/run/) commands at the [docker run reference](https://docs.docker.com/reference/run/)

## Use some command lines (on your own)

1. Check the available command line arguments: `$ docker help`
2. view available images: `$ docker images`
3. see all containers: `$ docker ps -a`
4. start a new container: `$ docker run -tid busybox`
    - get the container id: `$ docker ps`
    - run a command from the container: `$ docker exec <id> touch /home/helloworld`
    - attach to the container: `$ docker attach <id>`
    - verify the file we created exists & then exit with `CTRL-p CTRL-q`
    - stop the container: `$ docker stop <id>`
    - remove the container: `$ docker rm <id>`
    - verify it's gone: `$ docker ps -a`

## Troubleshooting

#### Environment variables

If you get an output like the one below:

```
$ docker ps
Cannot connect to the Docker daemon. Is 'docker -d' running on this host?
```

Make sure you have the correct environment variables exported as outlined above.



#### General Troubleshooting
One way to troubleshoot is to run the Docker daemon manually to see the logs in real-time.  

1. Make to sure SSH to the Boot2Docker image with ```boot2docker ssh```.  
2. Get the command that we run the Docker daemon with by running ```ps auxfw | grep docker```.  
3. Stop the Docker daemon with ```/etc/init.d/docker stop```.  
4. Manually run the Docker daemon with the command you found from ```ps``` which should be something similar to ```/usr/local/bin/docker -d -D -g /var/lib/docker -H unix:// -H tcp://0.0.0.0:2376 --tlsverify --tlscacert=/var/lib/boot2docker/tls/ca.pem --tlscert=/var/lib/boot2docker/tls/server.pem --tlskey=/var/lib/boot2docker/tls/serverkey.pem```.
5. Make sure to leave this process ```running``` and open another window for other operations.
