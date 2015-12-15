# Container OS Comparison
### 2016 Q1 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

---

# Common questions
> “Which is the best OS to run containers?”
> “Is it CoreOS? What about RedHat? I’ve also heard about something called RancherOS?”

Similar to the “Which Hypervisor is the best?” question
The answer is as always “it depends”

---

# What are the differences?

---

![fit](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/CoreOS.svg/2000px-CoreOS.svg.png)

---

# [CoreOS](https://coreos.com/)

 - Focuses on large-scale deployments, mostly targeting enterprises
 - Hundreds of contributors and over 500 IRC users in [#coreos on FreeNode](https://botbot.me/freenode/coreos/)
 - It comes bundled with interesting tools developed by the CoreOS team, such as etcd, fleet, and flannel
 - Great starting points to understand the concepts of service discovery, resource scheduling, and container networking
 - Auto-updates the OS and keeps an old version for rollback use cases

---

![fit](https://coreos.com/assets/images/media/Host-Diagram.png)

---

![fit](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/CoreOS_Architecture_Diagram.svg/2000px-CoreOS_Architecture_Diagram.svg.png)

---

# [CoreOS - Tectonic](https://tectonic.com/)
 - A joint venture by CoreOS and Google
 (Google Ventures is also an investor in CoreOS)
 - An interesting way of getting CoreOS running with Kubernetes quickly and efficiently
 - Tectonic is a commercial Kubernetes platform, which can be important if you’re looking for more than community support when running large-scale containers in production

---

![fit](http://rancher.com/wp-content/themes/arcade-basic/images/rancheros_logo.png)

---

# [RancherOS](http://rancher.com/rancher-os/)

- Takes what a container OS should be to the next step
- Everything in RancherOS is a Docker container
- A system Docker runs as PID 1 for system services
- A user Docker runs all the user containers
- Very lightweight, only 20MB

---

![fit](http://rancher.com/wp-content/themes/arcade-basic/images/rancheros_screenshot3.png)

---

# [Rancher](http://rancher.com/rancher/) on RancherOS

 Adds several functions on top of the OS, such as
 - Resource management
 - Container networking
 - Service discovery
 - Load balancing
 - Health checks and recovery
 - and more

---

# Snappy Ubuntu Core
![fit,background](http://assets.ubuntu.com/sites/ubuntu/1607/u/img/cloud/snappy/snappy.png)

---

# [Snappy Ubuntu Core](https://developer.ubuntu.com/en/snappy/)

 - Launched by Canonical in 2014
 - Comes with a new  application manager (“**snappy**”) that focuses on installing and running both apps and containers.
 - Apps live in read-only images (similar to container images)
 - Apps can be transactionally updated
 - Also an interesting base OS for containers themselves

---

![fit](https://raw.githubusercontent.com/projectatomic/atomic-site/master/source/images/logo.png)

---

## [RedHat Project Atomic](http://www.projectatomic.io/)

 - Built using upstream RPMs from CentOS, Fedora, and RHEL, and enables what RedHat calls “atomic” upgrades and rollback
 - Up to the admin to choose the base OS
 - Built-in functions for Docker, flannel, Kubernetes
 - Transactional OS update system, similar to CoreOS

---

![fit](https://mesosphere.com/wp-content/uploads/2015/06/facebook-share-default.png)

---

# [Mesosphere DCOS](https://mesosphere.com/)

 - A robust and innovative way of looking at how to manage large-scale deployments of resources and applications
 - Built using the open source projects Apache Mesos, Marathon, Zookeeper
 - Added enterprise features and functionality for containers and Big Data pipelines
 - Automatically handles failover for applications
 - Support for stateful scaleout services like Cassandra

---

![fit](https://vmware.github.io/photon/assets/img/photon-dfad9617.png)

---

# [VMware Photon OS](https://vmware.github.io/photon/)

 - Announced and released in April
 - The first part of an ongoing open-source effort called the VMware Photon Platform
 - Minimal OS meant to be used with VMware technologies such as VMFork
 - Compatible with container runtimes Docker, rkt and Pivotal Garden

---

# Learn more

 - Try them locally on your laptop or in a cloud environment
 - Docker workshops can be found at
  [https://github.com/emccode/training](https://github.com/emccode/training)
 - [Container management and CoreOS accreditation module](https://www.youtube.com/watch?v=-aQOGsHm_bo&index=8&list=PLbssOJyyvHuWiBQAg9EFWH570timj2fxt)
 - [Mesos accreditation module](https://www.youtube.com/watch?v=TkLPr3GexZU&list=PLbssOJyyvHuWiBQAg9EFWH570timj2fxt&index=6)
 - [Kubernetes accreditation module](https://www.youtube.com/watch?v=qCxYjq7EBHc&index=7&list=PLbssOJyyvHuWiBQAg9EFWH570timj2fxt)
 - Microservices and Service Discovery accreditation module
