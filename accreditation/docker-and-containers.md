# Docker and Containers
## 2015 Q2 EMC Accreditation
## Jonas Rosland & Matt Cowger

---

# Apps have fundamentally changed

---

# A decade ago (and still true for many)

Apps were monolithic

Built on a single stack such as .NET or Java

Long lived

Deployed to a single server

---

![fit](http://cantina.co/wp-content/uploads/2013/08/monolithic.jpg)

---

# Perhaps it was loadbalanced, but still monolithic

---

![fit](http://cantina.co/wp-content/uploads/2013/08/swimlanes.jpg)

---

# Today

Apps are constantly developed

New versions are being deployed often

Built from loosely coupled components

Deployed to a multitude of servers

---

![fit](http://cantina.co/wp-content/uploads/2013/08/SOA.jpg)

---

# How do you handle all these parts?

---

# Let's start with a useful analogy

---

# You're a shipping company

---

# You ship pianos

![](http://millerps.com/wp-content/uploads/2015/02/roland-v-piano-grand.jpg)

---

# You're great at it

---

# Then a customer wants to use you to ship potatoes as well

---

# You say "Ok, they'll fit next to the pianos"

---

![](http://millerps.com/wp-content/uploads/2015/02/roland-v-piano-grand.jpg)
![](http://www.ecokidsart.com/wp-content/uploads/2013/08/14272398-raw-potatoes-in-burlap-sack-isolated-on-white-background.jpg)

---

# Then another customer wants you to ship whiskey

---
![inline fill](http://www.ecokidsart.com/wp-content/uploads/2013/08/14272398-raw-potatoes-in-burlap-sack-isolated-on-white-background.jpg)![inline fill](http://renderstuff.com/publication-files/0222/big-image01-a.jpg)
![inline fill](http://millerps.com/wp-content/uploads/2015/02/roland-v-piano-grand.jpg)

---

# Things start to break when the whiskey spills all over the piano

---

# And your crew is wondering how to handle all the differences

---

# Size of goods

---

# Form of goods

---

# Requirements to keep it safe and stable during transport

---

# Being able to transport it using different transport methods

---

# So what to do?

---

# Enter, the Intermodal container

---

![fit](http://upload.wikimedia.org/wikipedia/commons/d/df/Container_01_KMJ.jpg)

---

# Now you can ship everything!

![](http://www.marineinsight.com/wp-content/uploads/2012/08/container-ship.jpg)

---

![](http://i941.photobucket.com/albums/ad252/RichReinhart/005_crop-4.jpg)

---

![](http://www.finnmoller.dk/rail-usa/bnsf-ca-cajonsub/bnsf4782-912-984-4669-frost-01.jpg)

---

# So what does this have to do with software?

---

# Well, it's similar

---

# You have an app built out of a lot of small parts

---

# These small parts are called micro services

---

![fit](http://clipart-finder.com/data/preview/web_server.png)

---

![fit](http://clipart-finder.com/data/preview/database_server.png)

---

![fit](http://clipart-finder.com/data/preview/baroquon_Shopping_Cart.png)

---

![fit](http://sfdata.startupweekend.org/files/2014/05/Fotolia_41498462_M1.jpg)

---

# You can surely install it in a production datacenter

---

# But would it look the same if you ran it in your dev environment?

---

# What about in a lab?

---

# Or in the cloud somewhere?

---

# Enter, the Container

---

# Containers make you app portable

 - It looks the same everywhere
 - No matter where you run it
 - Doesn't need you to install all the app dependencies on your host

---

# Docker is one container standard

![](http://blog.docker.com/wp-content/uploads/2013/06/Docker-logo-011.png)

---

# Docker has built a large ecosystem around it

---

# Docker facts

Launched in March 2013

Over 100 million downloads

Over 75 000 Dockerized applications

150+ Meetup Groups around the world

100+ case studies from companies such as eBay, Rackspace, New Relic, Gilt, Spotify, Cloudflare, Yandex, Cambridge Healthcare, Yelp and RelatelQ.

---

# Containers make your app shareable

 - The needs of the app is defined in a textfile
 - A "Dockerfile":
```
FROM        ubuntu:14.04
RUN         apt-get install -y redis-server
EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
```

---

# Containers contain everything your app needs

 - Binaries
 - Libraries
 - File system

---

# Containers use the host for certain things

 - Networking
 - Kernel

---

# So no need to run an entire OS (like in a VM) to run an app

---

# Summary

---

# Containers are awesome

You can use them for your next app

You can use thousands of already existing apps

They will always look the same

They are always portable

And they leave your host OS clean
