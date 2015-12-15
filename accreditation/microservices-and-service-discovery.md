# Microservices & Service Discovery
### 2016 Q1 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

---

_The microservices architectural style is an approach to developing a single application as a suite of small services, each running it's own process and communicating with lightweight mechanisms_
- Martin Fowler

---

# Monolithic app vs Microservices

---

# Enterprise application

- Often built using three parts
 - User interface
 - Database
 - Server-side application

- The server-side app will handle user requests, execute logic, retrieve and update data and show it to the user

The server-side app is what we call a **monolith**

---

# Monolithic != bad

A lot of successful applications have been and are still written as monoliths

But some apps are in need of faster change cycles, and that's usually were it breaks down

A small change made to a part of the application usually requires the entire monolith to be rebuilt and redeployed

Scaling the app requires running multiple copies of the entire application, which might not be the best idea or even possible

---

# Let's look at an example

---

# Monolithic application

![right, fit](http://cantina.co/images/blog/scaling-your-app-with-message-oriented-decoupled-architecture/monolithic.jpg)

---

# Scaling a monolithic application

![right,fit](http://cantina.co/images/blog/scaling-your-app-with-message-oriented-decoupled-architecture/swimlanes.jpg)

---

# Move to a microservices architecture

![right,fit](http://cantina.co/images/blog/scaling-your-app-with-message-oriented-decoupled-architecture/SOA.jpg)

---

# It's not just about scale, but also separation of concern

---

# Traditional organization layout

![fit,right](http://martinfowler.com/articles/microservices/images/conways-law.png)

---

# Business capability organization layout

![fit,right](http://martinfowler.com/articles/microservices/images/PreferFunctionalStaffOrganization.png)

---

# This also leads to new stacks

 - Developers can use the right tool for the job and are not necessarily locked into one tool or language
 - New processes are explored and applied
 - Innovation can happen quicker
 - New deployments can be done daily or weekly instead of taking months

---

# So how do we keep track of all the microservices?

---

# Service Discovery!

---

![fit](https://assets.digitalocean.com/articles/docker_ecosystem/Discover-Flow.png)

---

# What are some Service Discovery tools?

 - etcd, by CoreOS
 - Consul, by Hashicorp
 - Zookeeper, by Apache
 - SkyDNS (built on top of etcd)
 - Eureka, by Netflix
 - Smartstack, by AirBnB
 - All of them open source!

---

# Learn more

 - [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-an-introduction-to-common-components)
 - [Microservices by Martin Fowler](http://martinfowler.com/articles/microservices.html)
 - [Scaling your app with message oriented decoupled architecture by Cantina](http://cantina.co/scaling-your-app-with-message-oriented-decoupled-architecture/)
