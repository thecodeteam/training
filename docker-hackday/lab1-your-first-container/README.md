Run your first Docker container
===============================

# Description

In this lab you'll get to know how to use the boot2docker tool, how to search for Docker images on Docker hub, and how to run your images and connect to the applications inside them.

## Lab setup verification

Verify that you have the following software installed:

1. VirtualBox
2. Vagrant
3. boot2docker

Run the following commands to validate that your boot2docker installation is correct and working:

1. ```boot2docker init```
2. ```boot2docker up```
3. You should see something like this:

  ```
  $ boot2docker up
  Waiting for VM and Docker daemon to start...
  ...............ooo
  Started.
  Writing /Users/jonas/.boot2docker/certs/boot2docker-vm/ca.pem
  Writing /Users/jonas/.boot2docker/certs/boot2docker-vm/cert.pem
  Writing /Users/jonas/.boot2docker/certs/boot2docker-vm/key.pem

  To connect the Docker client to the Docker daemon, please set:
  export DOCKER_HOST=tcp://192.168.59.103:2376
  export DOCKER_CERT_PATH=/Users/jonas/.boot2docker/certs/boot2docker-vm
  export DOCKER_TLS_VERIFY=1
  ```

4. Copy and paste those three last lines to set all the correct environment variables.

## Using boot2docker

When using boot2docker, there are several things you can do.

If you just run the command ```docker``` you'll get a list of all the commands you can issue.

First off we want to have a look at the Docker installation information, so run:

```docker info```

This should give you an output similar to this:

```
Containers: 0
Images: 0
Storage Driver: aufs
Root Dir: /mnt/sda1/var/lib/docker/aufs
Dirs: 0
Execution Driver: native-0.2
Kernel Version: 3.16.7-tinycore64
Operating System: Boot2Docker 1.3.2 (TCL 5.4); master : 495c19a - Mon Nov 24 20:40:58 UTC 2014
Debug mode (server): true
Debug mode (client): false
Fds: 10
Goroutines: 13
EventsListeners: 0
Init Path: /usr/local/bin/docker
```

Here we can see how many images we have downloaded, and how many containers we have running, and more info like version of boot2docker etc.

The second command we'll look at is searching for images that we find interesting.

The [Docker hub](https://registry.hub.docker.com) currently has approximately **60000** images available for everyone to use freely.

Try a search for Sensu, a [really cool monitoring solution](http://sensuapp.org):

```docker search sensu```

You should get a list of Docker images that have been published and shared by the community, like this:

```
$ docker search sensu
NAME                                  DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
hiroakis/docker-sensu-server                                                          6                    [OK]
steeef/sensu-centos                   Sensu server on CentOS 6.x Forked from htt...   1                    [OK]
sstarcher/sensu-docker                                                                0                    [OK]
```

Try some other searches, like for redis, apache, nginx, mysql, postgresql, you name it, try to see if there are Docker images out there. Make note though that currently there are only linux applications and services out there. If you find an application or service that's not on the Docker hub, perhaps you could create one and be the first!

Now let's try to download an image using the ```docker pull``` command:

```docker pull ubuntu```

You'll see that Docker starts downloading a Docker image, this specific one is a base Ubuntu image. We'll try other images with more applications later.

When download is complete, you can run this image like this:

```docker run -i -t ubuntu /bin/bash```

What does this command do? Check the documentation for a specific Docker command by running it without any options, like:

```docker run```

You'll see that ```-i``` means we'll run this container interactively, and ```-t``` means we're attaching a pseudo-TTY to it (essentially attaching a terminal), then giving Docker the name of the image we want to run, and a command within that image.

This will start the container, giving it its own filesystem, networking etc. and start up a shell for us to rummage around inside the container. Pretty cool!

Now that you're in your container, look around abit and run some commands, like ```ifconfig``` and ```ls /```. You can even install applications here, so try to run ```apt-get update``` and then ```apt-get install apache```.

You now have apache running in a container!

To exit the container, there are two options. ```CTRL-d``` exits the shell and shuts down the container. If you want to keep the container running but detach from it, do ```CTRL-p CTRL-q```.

## Run some simple apps

Add more info here.


## Troubleshooting

If you see:

```
$ docker search sensu
2014/12/12 09:39:42 Cannot connect to the Docker daemon. Is 'docker -d' running on this host?
```

You probably haven't set the environment variables correctly. See [Lab setup verification](#lab-setup-verification)
