# CoreOS 101

### Jonas Rosland
### Developer Advocate
#### @virtualswede
#### jonas.rosland@emc.com
#### emccode.github.io
#### December 2014

^ Run this presentation with [Deckset](http://www.decksetapp.com/)

---

## CoreOS

Based on Gentoo
Kernel + Containers, nothing else
Built for running HA environments
Updates applied automatically

![inline](https://coreos.com/assets/images/brand/coreos-wordmark-horiz-color.png)

---

## Containers

Docker, of course, but also others like LXC and nspawn
Isolation from other applications
Link containers together
Less overhead than VMs

Released container runtime engine Rocket recently

![right, 120%](https://coreos.com/assets/images/media/Host-Diagram.png)

---

## systemd

System management daemon
Services, timers and one-off jobs
Logging through journal

---

## etcd

Highly available Key-Value database store
Provides service discovery and shared configurations
Others like it are Consul and Zookeeper
Provides a locking mechanism for safe(r) automatic updates

Public etcd service:
```
https://discovery.etcd.io/
```
This is frickin awesome, as you'll see :)

---

## etcdctl command

```
$ set services/db1 10.0.0.101
$ set services/db2 10.0.0.102
$ set services/db-master db1
```

```
$ get services/db-master
  "db1"
$ get services/db1
  "10.0.0.101"
```

---

## etcd automatic registration

![inline, white, 78%](https://coreos.com/assets/images/media/container-lifecycle.png)

---

![inline](https://coreos.com/assets/images/media/Three-Tier-Webapp.png)

---

## fleet

Deploy docker containers on arbitrary hosts in a cluster
Distribute services across a cluster using machine-level anti-affinity
Maintain N instances of a service
Re-scheduling on machine failure
Discover machines running in the cluster

---

## fleet

![inline](https://coreos.com/assets/images/media/Fleet-Scheduling.png
)

---

## Putting it all together

1. Create a systemd file for your service
2. Start the service using fleet
3. Register services in etcd
4. ...
5. Profit!

---

# Demotime!
