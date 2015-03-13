# Docker Ecosystem

### Jonas Rosland
### Developer Advocate
#### @virtualswede
#### jonas.rosland@emc.com
#### emccode.github.io
#### March 2015

---

# Basics of a container

---

![fit](https://assets.digitalocean.com/articles/docker_ecosystem/Container-Overview.png)

---

# Service Discovery

---

![fit](https://assets.digitalocean.com/articles/docker_ecosystem/Discover-Flow.png)

---

# Examples

service discovery / globally distributed key-value store
 - **etcd**
 - **consul**
 - **zookeeper**

**crypt**: project to encrypt etcd entries

**confd**: watches key-value store for changes and triggers reconfiguration of services with new values

---

# Networking tools

---

# Examples

**flannel**: Overlay network providing each host with a separate subnet

**weave**: Overlay network portraying all containers on a single network

**pipework**: Advanced networking toolkit for arbitrarily advanced networking configurations

---

# SocketPlane

_Acquired by Docker 4 days ago_

Open vSwitch Integration

ZeroConf multi-host networking for Docker

Elastic growth of a Docker/SocketPlane cluster

Support for multiple networks

Distributed IP Address Management (IPAM)

---

# Scheduling, Cluster Management and Orchestration

---

![fit](https://assets.digitalocean.com/articles/docker_ecosystem/Example-Schedule-App-F.png)

---

# Examples

**fleet**: scheduler and cluster management tool

**marathon**: scheduler and service management tool

**Swarm**: scheduler and service management tool

---

# More examples

**mesos**: host abstraction service that consolidates host resources for the scheduler

**kubernetes**: advanced scheduler capable of managing container groups

**compose**: container orchestration tool for creating container groups

---

# More info

https://www.mindmeister.com/389671722/docker-ecosystem

https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-an-introduction-to-common-components
