# Container Management: Kubernetes
## 2015 Q3 EMC Accreditation
## Jonas Rosland & Matt Cowger

---

# Kubernetes
## Container management at scale

---

# More than just "running" containers

Scheduling - where should my job be run
lifecycle
discovery
constiencu
scale-up
auth
monitoring
health

---

# Kubernetes
Container orchestration
Runs docker containers
Supports multiple clouds and bare-metal environments
Inspired and informed by Google's experiences and internal systems
Open Source and written in Go

---

# Primary concepts

0. Container - a sealed application package (Docker)
1. Pod - a small group pf tightly coupled containers
2. Controler - a loop that drives current state towards desired state
3. Service - a set of running pods that work together
4. Labels - identifying metadata attached to other objects
5. Selector - a query against labels, producinng a set result

---

# Pods

Small group of containers, tightly coupled
Shared namespace (share IP and localhost)
Ephemeral (can die and be replaced)
The smallest thing that can be scheduled, it's the "atom" of Kubernetes

---

# Why pods?

By coupling things together they can work better

---
