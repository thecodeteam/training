# DevOps tools: Vagrant and Packer
### 2015 Q3 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

---

# Hashicorp

![fit](https://pbs.twimg.com/profile_images/525656622308143104/0pPm3Eov.png)

---

# Hashicorp

Founded in 2012

Creates Open Source software like:
 - Vagrant
 - Packer
 - Serf
 - Consul
 - Terraform
 - Vault

---

![fit](http://upload.wikimedia.org/wikipedia/commons/8/87/Vagrant.png)

---

![fit](https://d23f6h5jpj26xu.cloudfront.net/mitchellh_24702982422030_small.png)

---

## Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops

---

![130%](images/kubernetes-graph-01.png)

---

# What is it?

An open source container orchestration system

Runs Docker containers

Supports multiple cloud and bare-metal deployments

Made to manage **applications**, not machines

---

# Kubernetes concepts

---

# Container

Sealed application package (Docker)

![inline](https://d3oypxn00j2a10.cloudfront.net/0.19.1/images/pages/brand_guidelines/small_v.png)

---

# Clusters

The compute resources on top of which your containers are built

Kubernetes can run anywhere!

![inline](images/kubernetes-install.png)

---

# Pods

Small group of Docker containers that work together

The smallest deployable unit that can be created, scheduled, and managed with Kubernetes

Example: web server and a content syncer

![inline](http://upload.wikimedia.org/wikipedia/commons/5/5b/NCI_peas_in_pod.jpg)

---

# Replication controllers

Ensures that a specified number of pods are running at any given time

Creates or kills pods as required

If you want to have 4 copies of something running, that's the desired state

The RCs always make sure to get to the desired state

---

# Services

A set of pods that work together

Example: load-balanced backends

---

# Labels

Used to organize and select groups of objects based on **key:value** pairs.

Examples:
```
role: frontend
vs
role: backend
```

---

# So to put it all together

Containers run on clusters

Pods are containers that work together

Services are pods that work together

Labels are used to organize services

---

![fit](images/Kubernetes overview.001.png)

---

![fit](images/Kubernetes overview.002.png)

---

![fit](images/Kubernetes overview.003.png)

---

![fit](images/Kubernetes overview.004.png)
