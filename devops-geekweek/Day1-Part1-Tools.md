#DevOps Agile Geek Week

>Software does not scale. Software teams do not scale. Architecture should be as much about enabling small teams to work on small components as the technical requirements of the software.

---

#What You'll Learn

* How to 'do' Agile
* How *not* to 'do' Agile
* Agile/DevOps related tools
* IaaS and PaaS basics
* How to talk about this in the real world

---

#Themes

- Automation
- Text Configuration (JSON/YAML)
  - machine parseable, human readable
- Everything in Git
- Local Tools = Production Environments - Scale
- Free/Opensource Tools

---

#Day 1 Agenda

* Get Acclimated to Tools
* What is / how to do Agile
* Sprint Planning

---

#Tools

- [Git](https://help.github.com/articles/set-up-git/)
- [Vagrant](http://vagrantup.com)
- [VirtualBox](http://virtualbox.org)
- [CloudFoundry CLI](http://docs.cloudfoundry.org/devguide/installcf/)
- [Slack](http://slack.com)
- [Trello](http://www.trello.com)

you should have these installed already (they were your homework)

---

#Git

a distributed version control system, where every user has a complete and full copy of the source code.  

if you can't check it in, you can't keep track of it, so you can't version it, so you can't automate it.  *everything* belongs in source code control, and git is the standard in 3rd platform.  other possible options: subversion (svn), mercurial (hg), Perforce (p4), ClearCase (cc).

##GitHub?

A freemium service to host Git repositories (repos).  Public repos are free, private ones are $$$

---

#Vagrant

A tool for managing sets of virtual machines that comprise an application, defined as text (so they can be versioned in Git!).

```
Vagrant.configure("2") do |config|
  if Vagrant.has_plugin?("vagrant-proxyconf")
    # config.proxy.http     = "http://proxy.vmware.com:3128/"
    # config.proxy.https    = "http://proxy.vmware.com:3128/"
    # config.proxy.no_proxy = "localhost,127.0.0.1,.vmware.com"
  end
  scaleio_nodes.each do |node|
    config.vm.define node[:hostname] do |node_config|
      node_config.vm.box = "#{vagrantbox}"
      node_config.vm.box_url = "#{vagrantboxurl}"
      node_config.vm.host_name = "#{node[:hostname]}.#{domain}"
      node_config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
```

---

#CloudFoundry CLI

A command line tool for managing CloudFoundry applications and related services.  Again, all CLI so that it can be scripted and automated.

---

#Slack

Think of it like IRC on 'roids'.  Team chat with multiple channels, integrations with services, etc.  Mobile tools.

Often used to significantly replace email within Agile teams

---

#Trello

An online 'Kanban' board to track tasks and completion.  
