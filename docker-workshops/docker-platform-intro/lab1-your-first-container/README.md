Run your first Docker container
===============================

# Description

In this lab you'll get to know how to use the Docker Machine tool, how to search for Docker images on Docker hub, and how to run your images and connect to the applications inside them.

## Lab setup verification

Verify that you have the following software installed:

1. A 64-bit OS
2. [Docker Toolbox](https://www.docker.com/toolbox)

(Sidenote: If you want to get into managing your apps in a more interesting way have a look at [Homebrew](http://brew.sh/) and [Homebrew Cask](http://caskroom.io/) for OS X, and [Chocolatey for Windows](https://chocolatey.org/packages/docker).)

Docker Machine will create a virtual machine for us where we can run our docker containers, since you cannot run Docker containers or bare OS X or Windows. This part isn't needed if you're running a Linux desktop.

Let's set up our first container host!

```
$ docker-machine create --driver virtualbox containerhost
Creating VirtualBox VM...
Creating SSH key...
Starting VirtualBox VM...
Starting VM...
To see how to connect Docker to this machine, run: docker-machine env containerhost
```

You now have a container host ready to use, let's make sure we can connect to it.

```
$ docker-machine env containerhost
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:2376"
export DOCKER_CERT_PATH="/Users/jonas/.docker/machine/machines/containerhost"
export DOCKER_MACHINE_NAME="containerhost"
# Run this command to configure your shell:
# eval "$(docker-machine env containerhost)"
```

Now copy & paste either the `export` lines, or run the `eval` command. Both will make sure your shell is correctly configured to connect to the correct container host.

## Using Docker

Now that you have a container host there are several things you can do.

If you just run the command `docker` you'll get a list of all the commands you can issue.

First off we want to have a look at the Docker installation information, so run:

`docker info`

This should give you an output similar to this:

```
$ docker info
Containers: 0
Images: 0
Storage Driver: aufs
 Root Dir: /mnt/sda1/var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 0
 Dirperm1 Supported: true
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 4.0.9-boot2docker
Operating System: Boot2Docker 1.8.1 (TCL 6.3); master : 7f12e95 - Thu Aug 13 03:24:56 UTC 2015
CPUs: 1
Total Memory: 996.2 MiB
Name: containerhost
ID: 4ZKQ:2L2G:SY3X:XQUN:DQEE:OSWN:4JL2:5WIW:SKGO:DG2Z:YZAU:ORYB
Debug mode (server): true
File Descriptors: 9
Goroutines: 16
System Time: 2015-09-17T16:12:42.43394229Z
EventsListeners: 0
Init SHA1:
Init Path: /usr/local/bin/docker
Docker Root Dir: /mnt/sda1/var/lib/docker
Username: virtualswede
Registry: https://index.docker.io/v1/
Labels:
 provider=virtualbox
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

What does this command do? Check the documentation for a specific Docker command by running it without any options, like:

`docker run`

You'll see that `-i` means we'll run this container interactively, and `-t` means we're attaching a pseudo-TTY to it (essentially attaching a terminal), then giving Docker the name of the image we want to run, and a command within that image.

This will start the container, giving it its own filesystem, networking etc. and start up a shell for us to rummage around inside the container. Pretty cool!

Now that you're in your container, look around a bit and run some commands, like `ifconfig` and `ls /`. You can even install applications here, so try to run `apt-get update` and then `apt-get install apache2`.

You now have apache running in the container!

To exit the container, there are two options. `CTRL-d` exits the shell and shuts down the container. If you want to keep the container running but detach from it, do `CTRL-p CTRL-q`. You can then re-attach to it by running `docker attach UNIQUEID`.

## Run some simple apps

We will run tomcat which a Java based application server. To do this we use the following command.

```docker run -d -p 8888:8080 tomcat:8.0```

The image will be downloaded if required and tomcat will be run in a *deamon* mode.

Now run the following command.

```docker ps```

Which will yield an output that looks something like below (Partial output).

```
STATUS              PORTS                    NAMES
Up 17 seconds       0.0.0.0:8888->8080/tcp   romantic_stallman
```
Notice that under the PORTS section the port 8888 of the localhost is forwarded to port 8080 of tomcat running in the container.

You can run your apps by pointing your browser to ```localhost:8888``` or you can just verify using the following curl commands.

```curl -L $(boot2docker ip 2>/dev/null):8888```

```curl -L $(boot2docker ip 2>/dev/null):8888/examples```

## Build your own container

Building containers is easy, and we'll show how to by using a Dockerfile.

A Dockerfile is just a simple textfile with information about what to start from (a linux distro usually), what commands to run before it's complete (installing packages and changing configuration files for instance), what port to open and lastly what binary to run.

There are more settings of course, and we'd recommend you to read up on them [here](https://docs.docker.com/).

An easy container to build is the Redis key-value store service. Read through the steps [outlined here](https://docs.docker.com/examples/running_redis_service/).

## Troubleshooting

#### Environment variables

If you get an output like the one below:

```
$ docker ps
Cannot connect to the Docker daemon. Is 'docker -d' running on this host?
```

Make sure you have the correct environment variables exported as outlined above.

#### Certificate and Trust Issues
There are two encryption paths that must be considered.  There is TLS encryption going from the Docker client running on your laptop to the container host Docker daemon.  There is also TLS encryption running from the Docker daemon within the container host to the public Docker Hub/CDN.

If you have problems with your client there are likely two issues.

1. Check that you can reach the container host by checking the IP with `ping $(docker-machine ip containerhost)`.  If this doesn't work then you probably need to add a route for the `192.168.99.x` traffic to the proper VBoxNet interface.  This issue is usually caused by Cisco VPN so make sure you're disconnected from the VPN and some times a proper restart is needed.  Run an `ifconfig` to identify which is the proper interface and then run ```sudo route -n add -net 192.168.99.0/24 -interface vboxnetX``` for the proper interface.
>As a side note, you can communicate to the container host via a `NAT` and `BRIDGED` method.  The `NAT` method means that you can leverage the `127.0.0.1` address of your laptop and it forwards appropriate ports to a static IP of your container host.  The method we are using for this workshop is the `BRIDGED` mode and uses a `routed` IP.

2. You probably haven't set the environment variables correctly. See [Lab setup verification](#lab-setup-verification)

### For EMC employees only

If you have a problem when running `docker run` or `docker pull` where it hangs when pulling docker image layers and you are inside the EMC corporate network, it is likely that you are running into SSL certificate errors and trust issues between the Docker daemon and the public Docker Hub/CDN.  For this you must download our SSL certificate and place it inside the container host.

- Open `http://gso.corp.emc.com/installupdatedcerts.aspx` and Download `EMCs SSL Decryption` certificate.
- Open the file in a text editor and copy the contents
- Run `docker-machine ssh containerhost` to SSH into the container host
- Stop Docker by running `ps ax | grep docker` to find the process ID, and then kill it by running `sudo kill processID`
- In the Docker container host, create a new file and copy the `EMC SSL.cer` contents into it by running `vi EMC_SSL.cer`, press `i` to be able to insert text, paste the contents you copied above, then press `:wq` to write the file and quit the text editor
- Convert the certificate to a PEM file with `openssl x509 -in EMC_SSL.cer -out EMC_SSL.pem`
- Update the CA certificates files to include this certificate with `cat EMC_SSL.pem | sudo tee -a /etc/ssl/certs/ca-certificates.crt`
- Start the Docker daemon services again with ```sudo /etc/init.d/docker start```
- Verify that you can still connect to the Docker engine by running `docker version` and then verify that you can download images by doing `docker pull redis`

#### General Troubleshooting
One way to troubleshoot is to run the Docker daemon manually to see the logs in real-time.  

1. Make to sure SSH to the Boot2Docker image with ```boot2docker ssh```.  
2. Get the command that we run the Docker daemon with by running ```ps auxfw | grep docker```.  
3. Stop the Docker daemon with ```/etc/init.d/docker stop```.  
4. Manually run the Docker daemon with the command you found from ```ps``` which should be something similar to ```/usr/local/bin/docker -d -D -g /var/lib/docker -H unix:// -H tcp://0.0.0.0:2376 --tlsverify --tlscacert=/var/lib/boot2docker/tls/ca.pem --tlscert=/var/lib/boot2docker/tls/server.pem --tlskey=/var/lib/boot2docker/tls/serverkey.pem```.
5. Make sure to leave this process ```running``` and open another window for other operations.


If docker-machine is hung on "starting vm..." and you're on a Mac, it might be due to a conflict with Kitematic (if you have it installed). Steps to resolve:

1. Ctrl+C out of it.
2. Delete the new machine ```docker-machine rm containerhost```
3. Restart the virtualbox interface ```sudo ifconfig vboxnet0 down``` and then ```sudo ifconfig vboxnet0 up```
4. Lastly recreate it again: ```docker-machine create --driver virtualbox containerhost```
