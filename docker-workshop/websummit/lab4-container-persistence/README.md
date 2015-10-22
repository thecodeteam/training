Lab IV: Persist a container's state and data
===============================

## Description

In this lab you'll learn how to persist data between container instances.

### Lab setup

Each of you has been handed a piece of paper with a machine that has Docker and REX-Ray installed. SSH into your machine

#### Mac/Linux
Use Terminal
`$ ssh student@IPADDRESS`

#### Windows
Use PuTTy

## Persist Data Between Containers
** small presentation on why persistence** 

Each machine has [REX-Ray](https://github.com/emccode/rexray) installed which is a SDS cli control tool. It is currently configured for AWS usage.

Let's take a quick tour of REX-Ray commands and see how we can manage storage. Use `rexray help` to see the available commands. We will work in reverse order.

To view the types of storage drivers available, use the `rexray adapter types` command to see a similar output:
```
$ rexray adapter types
Storage Driver: XtremIO
Storage Driver: docker
Storage Driver: linux
Storage Driver: ec2
Storage Driver: Openstack
Storage Driver: Rackspace
Storage Driver: ScaleIO
```

REX-Ray is also a system level service. You can `start`, `stop`, `restart`, and get the `status`. To the available commands type `rexray service --help`. Do not run these commands during the lab exercise.

`rexray device` commands are used to format, mount, and unmount devices on the local filesystem. We will not need to use any of these commands for this lab exercise. However, perform `rexray device get` to retrieve a list of all the mounts on the host. You will recieve something similar to:
```
INFO[0000] getting mounts                                deviceName= driverName=linux mountPoint=
- id: 17
  parent: 22
  major: 0
  minor: 15
  root: /
  mountpoint: /sys
  opts: rw,nosuid,nodev,noexec,relatime
  optional: ""
  fstype: sysfs
  source: sysfs
  vfsopts: rw
- id: 18
  parent: 22
  major: 0
  minor: 3
  root: /
  mountpoint: /proc
  opts: rw,nosuid,nodev,noexec,relatime
  optional: ""
  fstype: proc
  source: proc
  vfsopts: rw
  ...
  ...
```

We will come back to the `rexray snapshot` manager a bit later (you can probably guess what that's for), for now lets checkout `rexray volume` manager to get started making volumes.

The first command to run is `rexray volume get`. We will get a long list of volumes because every host in this classroom is in the same AZ. That is why  volumes are represented as `""` but have unique `volume-id`s.

Lets see all the new volume creation flags using `rexray volume create --help`:

```
Flags:
      --availabilityzone="": availabilityzone
      --iops=0: IOPS
      --runasync[=false]: runasync
      --size=0: size
      --snapshotid="": snapshotid
      --volumeid="": volumeid
      --volumename="": volumename
      --volumetype="": volumetype
```

Create a new volume: `rexray volume create --size=5 --volumename="<studentID>"` For the examples, I will be using `student001`. By default, this will create a standard volumetype without any guarentee of IOPS in our AZ.
```
$ rexray volume create --size=10 --volumename="student001"
INFO[0000] Waiting for volume creation to complete
name: student001
volumeid: vol-2765e5cb
availabilityzone: us-east-1b
status: available
volumetype: standard
iops: 0
size: "12"
networkname: ""
attachments: []
```

Now it's time to use this inside of a docker container:
```
$ docker run -ti --name temp --volume-driver=rexray -v student001:/student001 busybox
```

once we are in our container, change directories to the `student001` folder and create a new file
```
/ # ls
bin         dev         etc         home        proc        root        student001  sys         tmp         usr         var
/ # cd student001/
/student001 # ls
/student001 # touch hellopersistence
```

exit the container with `option+c` and then completely kill the container with `docker rm temp`. At this point, the container no longer exists.

Create a new container by mounting the same volume:
```
$ docker run -ti --volume-driver=rexray -v student001:/student001 busybox
```

Navigate to the `student001` and you will see that our file has persisted. exit the container.

## Docker 1.9 New and Enhanced Features for Data Persistence
Now that we've seen [REX-Ray](https://github.com/emccode/rexray) be used, lets see how we can use Docker to control REX-Ray.

To make this function properly, use host `b`, or whichever host's Docker daemon has NOT been configured to point to the Swarm Master instance. There is currently a bug where a volume will be created for every host in the cluster if issued through a Docker Swarm Master.

Docker can now control volumes and the volume-driver. Instead of creating volumes directly from REX-Ray, we can create them with Docker:
```
$ docker volume create --driver=rexray --name=student001a --opt=volumetype=io1 --opt=iops=100 --opt=size=10
```

This command will take a few seconds, but the output will be the name of the volume that has been created. In this case, it will be `student001a`.

At this point, switch back over to host `a`.

Unlike the `rexray volume get` command, the `docker volume ls` command will return volumes on the host and the drive associated with it. **NOTE** if you are on host `a` it will also return the volume we created directly with REXray since it's being discovered through Swarm.
```
student001b@student001b:~/composetest$ docker volume ls
DRIVER              VOLUME NAME
rexray              student001a
local               6c3c2a3249651a0f5f72022f010d3b4dbd38e58d698a62714f491c524681a555
local               f3622f5cd30063764da8ada3680c4d4bd07409188e34333edc435069fc52dd60
local               91886bdf427bcc583aad2aa1e0a68b54c532a81ccb5b0d317b70204cb7da7836
```

Let's do the same thing as before to prove persistence but let's do it BETWEEN machines using constraints!

```
$ docker run -tid --name hosta -e ‘constraint:node==*a*’ --volume-driver=rexray -v student001a:/student001a busybox
$ docker ps
```

`docker ps` should show the name as the following `student001a/hosta`.

Attach to the host and create a new file.
```
$ docker attach hosta

/ # ls
bin          dev          etc          home         proc         root         student001a  sys          tmp          usr          var
/ # cd student001a/
/student001a # touch mynewawesomefile
/student001a # exit
```

The container has quit. start another one on host `b`
```
$ docker run -ti --name hostb -e ‘constraint:node==*b*’ --volume-driver=rexray -v student001a:/student001a busybox
```

go to the `student001a` directory and there is `mynewawesomefile`

Exit out a do a little clean up. 
```
$ docker volume rm student001
$ docker volume rm student001a
```

This lab has covered data persistence and new commands exposed in Docker 1.9!