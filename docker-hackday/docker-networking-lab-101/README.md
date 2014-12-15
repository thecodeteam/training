
Docker Networking (101) - Dec 2014
========================
![alt text][logo]
[logo]: https://d3oypxn00j2a10.cloudfront.net/0.12.10/img/nav/docker-logo-loggedout.png

## What you need
- **On Mac**
  - Install Boot2Docker, Virtualbox
  - https://github.com/boot2docker/osx-installer/releases
  - ```boot2docker download```
  - ```boot2docker init```
  - ```boot2docker up```
  - ```export DOCKER_HOST=tcp://<VM-IP>:2375```
  - or ```boot2docker ssh```


Introduction
===============

### What we will cover:
- The Docker Bridge & Veth Pairs
- Networking Modes
- Containers and IP Addresses
- How to Connect Containers
- How to Manage Ports
- How to Link Containers
- How to Create Services Between Containers
  - Mysql+Flask Example

The Docker Bridge & Veth Pairs
==============================

Docker uses a virtaual ethernet bridge to manage networking between container on 
a single host called ```docker0```. upon startup docker will randomly choose a 
subnet from the private range defined in RFC 1918 that are not used on the host machine. 
The docker bridge subnet may have the address similar to ```172.17.42.1/16``` which
gives the host 65,534 possible container ip addresses. the ".1" address
will be the gateway for the containers.

```ifconfig | grep -A 7 docker0```

There are various options to change the docker bridge and general docker networking,
 we will not cover them in detail here but the options include:
.* -b or --bridge=BRIDGE (Build your own bridge)
.* --bip=CIDR (Give the docker bridge your own CIDR address)
.* --fixed-cidr (Limit address range)
.* -H SOCKET --host=SOCKET (Tell the server to listen on)
.* --icc=true|false (Enable/Disable communication between containers)
.* --ip=IPADDRESS (Port forwards go to a single address, instead of 0.0.0.0)
.* --ip-forward=true|false
.* --iptables=true|false
.* --mtu=BYTES

###### NAT
See what forwarding rules exists on your Docker-host

```sudo iptables -t nat -L -n```

###### V-Eth Pairs
Every time Docker creates a container, it creates a pair of peer interfaces that are
like opposite ends of a pipe (i.e., a packet sent on one will be received on the
other). It gives one of the peers to the container to become its eth0 interface and
keeps the other peer, with a unique name like vethec6a, out on the host machine. Consider
one end to be "plugged" into the container and the other into the docker0 bridge.

###### See your veths
```
ifconfig | grep veth
veth4ea42c9 Link encap:Ethernet  HWaddr 2A:39:65:D0:0F:CB
vethd8887a8 Link encap:Ethernet  HWaddr BA:A7:38:FB:AF:0F
```

Networking Modes
================

Docker allows containers to change some networking properties during runtime. This allows certain networking features to be enabled or changed for individual containers.

```
--net="bridge"   Set the Network mode for the container
                 'bridge': creates a new network stack for the container on the docker bridge
                 'none': no networking for this container
                 'container:<name|id>': reuses another container network stack
                 'host': use the host network stack inside the container.  Note: the host mode gives the container full access to local system services such as D-bus and is therefore considered insecure.
```

In this lab, we will stick to using "bridge" to provide the containers a local subnet.

Containers and IP Addresses
===========================

All containers will get an IP address when deployed when they use the default docker bridge. Lets test this out, lets deploy a simple web application.

```
sudo docker run -rm -it ubuntu /bin/bash
```

(you may need to **apt-get install net-tools** )
```
69163446b74b:/# ifconfig
eth0      Link encap:Ethernet  HWaddr 02:42:0a:00:00:16
          inet addr:172.17.0.7  Bcast:0.0.0.0  Mask:255.255.255.0
          inet6 addr: fe80::42:aff:fe00:16/64 Scope:Link
          UP BROADCAST RUNNING  MTU:1500  Metric:1
          RX packets:12 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:936 (936.0 B)  TX bytes:468 (468.0 B)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
```

Or from outside of the container.
```
sudo docker inspect -f '{{ .NetworkSettings.IPAddress }}' <name>
172.17.0.7
```

Without any networking
```
docker run -rm -it -P --net=none ubuntu /bin/bash
Warning: '-rm' is deprecated, it will be replaced by '--rm' soon. See usage.
root@a5d337f58977:/# ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
```

With host networking
```
docker run -rm -it -P --net=host ubuntu:13.10 /bin/bash
Warning: '-rm' is deprecated, it will be replaced by '--rm' soon. See usage.
root@boot2docker:/# ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN mode DEFAULT
    link/ether 0a:f5:33:2a:cc:9f brd ff:ff:ff:ff:ff:ff
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 1000
    link/ether 08:00:27:37:d7:d5 brd ff:ff:ff:ff:ff:ff
4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 1000
    link/ether 08:00:27:d8:c0:d7 brd ff:ff:ff:ff:ff:ff
5: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
    link/ether 56:84:7a:fe:97:99 brd ff:ff:ff:ff:ff:ff
15: vethd8887a8: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP mode DEFAULT
    link/ether ba:a7:38:fb:af:0f brd ff:ff:ff:ff:ff:ff
17: veth4ea42c9: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP mode DEFAULT
    link/ether 2a:39:65:d0:0f:cb brd ff:ff:ff:ff:ff:ff
```

How to Manage Ports
===================
Docker exposes port managment in two main ways, via the Dockerfile and during runtime.

### Dockerfile
//TOOD

### Runtime
//TODO

How to Link Containers
======================
//TODO

How to Create Services Between Containers
=========================================
//TODO

Future Networking & Docker Proposals
===================================

- Native Multi-host Networking
  - https://github.com/docker/docker/issues/8951
- Network Drivers
  - https://github.com/docker/docker/issues/8952
- Plugins
  - https://github.com/docker/docker/pull/8968

