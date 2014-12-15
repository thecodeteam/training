Multi-container apps with CoreOS
================================

## Description

In this lab you'll learn how to setup CoreOS, how to use fleet and deploy several containers and link them together as one application.

## Lab setup verification

Verify that you have the following software installed:

1. VirtualBox
2. Vagrant
3. Git
4. [CoreOS Vagrant setup](https://coreos.com/docs/running-coreos/platforms/vagrant/) by running


## Setting up a 3 node CoreOS cluster with Vagrant

Follow the steps found [here](https://coreos.com/docs/running-coreos/platforms/vagrant/). Essentially do the following:

1. Enter the coreos-vagrant directory
2. Copy config.rb.sample to config.rb
3. Edit config.rb and set ```$num_instances=3``` and ```$update_channel='stable'```
4. Go to [https://discovery.etcd.io/new](https://discovery.etcd.io/new) and copy your discovery token.
5. Copy user-data.sample to user-data
6. Edit user-data and set your discovery token like ```discovery: https://discovery.etcd.io/YourTokenHere```
7. Run ```vagrant up```
8. After a while you can now connect the your CoreOS by running ```vagrant ssh core-01 -- -A```

## Running containers in CoreOS

Please read the [documentation](https://coreos.com/docs/launching-containers/launching/launching-containers-fleet/) and follow along with the instructor.
We'll cover running one container in a CoreOS cluster, verify failover functionality, create a multi-container HA setup, and get used to working with so called sidekicks and the etcd service discovery.

## Troubleshooting
