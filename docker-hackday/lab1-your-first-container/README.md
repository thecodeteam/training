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

The first command we'll look at is searching for images that we find interesting.

The [Docker hub](https://registry.hub.docker.com) as of todays date has approximately 60000 images available for everyone on their Docker hub.

Try a search for Sensu, a really cool monitoring solution:

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


## Troubleshooting

If you see:

```
$ docker search sensu
2014/12/12 09:39:42 Cannot connect to the Docker daemon. Is 'docker -d' running on this host?
```

You probably haven't set the environment variables correctly. See [Lab setup verification](## Lab setup verification)
