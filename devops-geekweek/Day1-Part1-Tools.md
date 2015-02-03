#DevOps Agile Geek Week

>Software does not scale. Software teams do not scale. Architecture should be as much about enabling small teams to work on small components as the technical requirements of the software.

^ Open this presentation with [Deckset](http://www.decksetapp.com/)

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
- Free/Open Source Tools

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
- [Boot2Docker](http://boot2docker.io/)
- [CloudFoundry CLI](http://docs.cloudfoundry.org/devguide/installcf/)
- [Slack](http://slack.com)
- [Trello](http://trello.com)

---

#Git

A distributed version control system, where every user has a complete and full copy of the source code.  

If you can't check it in, you can't keep track of it, so you can't version it, so you can't automate it.

*Everything* belongs in source code control, and git is the standard in 3rd platform.

Other possible options: subversion (svn), mercurial (hg), Perforce (p4), ClearCase (cc).

---

##GitHub?

A freemium service to host Git repositories (repos). Public repos are free, private ones are still cheap.

Most open source projects are hosted and collaborated on here.

> If you're not on GitHub you don't exists.
-- Friendly developer

---

#Vagrant

A tool for managing sets of virtual machines that comprise an application, defined as text (so they can be versioned in Git!).

```
Vagrant.configure("2") do |config|
  scaleio_nodes.each do |node|
    config.vm.define node[:hostname] do |node_config|
      node_config.vm.box = "#{vagrantbox}"
      node_config.vm.box_url = "#{vagrantboxurl}"
      node_config.vm.host_name = "#{node[:hostname]}.#{domain}"
      node_config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
        ...
```

---

#CloudFoundry CLI

A command line tool for managing CloudFoundry applications and related services.  Again, all CLI so that it can be scripted and automated.

Simple commands to deploy, scale and monitor applications.

---

#Slack

Think of it like IRC on 'roids'. Team chat with multiple channels, integrations with services like GitHub, Trello, etc.

Often used to significantly replace email within Agile teams.

---

#Trello

An online 'Kanban' board to track tasks and completion.

Very simple and user friendly, can be used for anything from sprint management to planning a birthday party.
