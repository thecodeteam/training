#DevOps Agile Geek Week

>Software & Infra do not scale. Software & Infra teams do not scale. Architecture should be as much about enabling small teams to work on small components as the technical requirements of the software.

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

* Get acclimated to the [tools](Day1-Part1-Tools.md) in use
* Discuss basic Agile methodology and how to use it.
* Do first Sprint Planning for team project, including story pointing.


---

#Tools

[Git](https://help.github.com/articles/set-up-git/)
[CloudFoundry CLI](http://docs.cloudfoundry.org/devguide/installcf/)
[Slack](http://slack.com)
[Trello](http://trello.com)

Optional
  - [Vagrant](http://vagrantup.com)
  - [VirtualBox](http://virtualbox.org)
  - [Boot2Docker](http://boot2docker.io/)

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
