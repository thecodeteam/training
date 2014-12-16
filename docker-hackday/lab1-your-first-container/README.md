Run your first Docker container
===============================

# Description

In this lab you'll get to know how to use the boot2docker tool, how to search for Docker images on Docker hub, and how to run your images and connect to the applications inside them.

## Lab setup verification

Verify that you have the following software installed:

1. VirtualBox
2. Vagrant
3. boot2docker

(Sidenote: If you want to get into managing your apps in a more interesting way have a look at [Homebrew](http://brew.sh/) and [Homebrew Cask](http://caskroom.io/) for OS X, and [Chocolatey for Windows](https://chocolatey.org/packages/docker).)

Run the following commands to validate that your boot2docker installation is correct and working:

1. ```boot2docker init```
2. ```boot2docker up```
3. You should see something like this:

  ```
  $ boot2docker up
  Waiting for VM and Docker daemon to start...
  ...............ooo
  Started.
  Writing /Users/<youruser>/.boot2docker/certs/boot2docker-vm/ca.pem
  Writing /Users/<youruser>/.boot2docker/certs/boot2docker-vm/cert.pem
  Writing /Users/<youruser>/.boot2docker/certs/boot2docker-vm/key.pem

  To connect the Docker client to the Docker daemon, please set:
  export DOCKER_HOST=tcp://192.168.59.103:2376
  export DOCKER_CERT_PATH=/Users/<youruser>/.boot2docker/certs/boot2docker-vm
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

When download is complete, your "Hello World" with Docker command looks something like this:

```docker run ubuntu echo hello world```

You can run other commands or invoke a bash shell like this:

```docker run -i -t ubuntu /bin/bash```

What does this command do? Check the documentation for a specific Docker command by running it without any options, like:

```docker run```

You'll see that ```-i``` means we'll run this container interactively, and ```-t``` means we're attaching a pseudo-TTY to it (essentially attaching a terminal), then giving Docker the name of the image we want to run, and a command within that image.

This will start the container, giving it its own filesystem, networking etc. and start up a shell for us to rummage around inside the container. Pretty cool!

Now that you're in your container, look around a bit and run some commands, like ```ifconfig``` and ```ls /```. You can even install applications here, so try to run ```apt-get update``` and then ```apt-get install apache2```.

You now have apache running in the container!

To exit the container, there are two options. ```CTRL-d``` exits the shell and shuts down the container. If you want to keep the container running but detach from it, do ```CTRL-p CTRL-q```.

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

```curl -L $(boot2docker ip):8888```

```curl -L $(boot2docker ip):8888/examples```

## Troubleshooting

#### Environment variables

```
$ docker search sensu
2014/12/12 09:39:42 Cannot connect to the Docker daemon. Is 'docker -d' running on this host?
```
<br>
#### Certificate and Trust Issues
There are two encryption paths that must be considered.  There is TLS encryption going from the Docker client running on your laptop to the Boot2Docker Docker daemon.  There is also TLS encryption running from the Docker daemon within Boot2Docker to the public Docker Hub.

If you have problems with your client ther are likely two issues.

1. Check that you can reach the Boot2Docker image by checking the IP with ```ping $(Boot2Docker ip)```.  If this doesn't work then you probably need to add a route for the ```192.168.59.x``` traffic to the proper VBoxNet interface.  This issue is caused by Cisco VPN.  Run an ```ifconfig``` to identify which is the proper interface and then run ```sudo route -n add -net 192.168.59.0/24 -interface vboxnetX``` for the proper interface.

As a side note, you can communicate to the Boot2Docker image via a ```NAT``` and ```BRIDGED``` method.  The ```NAT``` method means that you can leverage the ```127.0.0.1``` address of your laptop and it forwards appropriate ports to a static IP of Boot2Docker.  The method we were describing before that the ```Docker``` client uses is the ```BRIDGED``` mode since it uses a ```routed``` IP.

2. You probably haven't set the environment variables correctly. See [Lab setup verification](#lab-setup-verification)
<br>
<br>
If you have a problem when running ```docker run``` where it pauses when downloading FS layers and you are in the EMC corporate network, it is likely that you are running into SSL certificate errors and trust issues between the Docker daemon and the public Docker Hub/CDN.  For this you must donwload our SSL certificate and place it on the Boot2Docker image.

- Open ```http://gso.corp.emc.com/installupdatedcerts.aspx``` and Download ```EMCs SSL Decryption``` certificate.
- Convert the certificate to a PEM file with ```openssl x509 -in ~/Downloads/EMC\ SSL.cer -out EMC_SSL.pem```
- SSH to the Boot2Docker image to place the certificate there since it makes the SSL calls with ```boot2docker ssh```
- Update the CA certificates files to include this certificate with ```cat EMC_SSL.pem | sudo tee -a /etc/ssl/certs/ca-certificates.crt```
- Restart the Docker daemon services with ```sudo /etc/init.d/docker restart```

#### General Troubleshooting
One way to troubleshoot is to run the Docker daemon manually to see the logs in real-time.  
1. Make to sure SSH to the Boot2Docker image with ```boot2docker ssh```.  
2. Get the command that we run the Docker daemon with by running ```ps auxfw | grep docker```.  
3. Stop the Docker daemon with ```/etc/init.d/docker stop```.
4. Manually run the Docker daemon with the command you found from ```ps``` which should be something similar to ```/usr/local/bin/docker -d -D -g /var/lib/docker -H unix:// -H tcp://0.0.0.0:2376 --tlsverify --tlscacert=/var/lib/boot2docker/tls/ca.pem --tlscert=/var/lib/boot2docker/tls/server.pem --tlskey=/var/lib/boot2docker/tls/serverkey.pem```.
5. Make sure to leave this process ```running``` and open another window for other operations.

<br><br>


