#Cloud Foundry on OpenStack Hands-On Labs

##Prerequisites

Needless to say you'll need a laptop! For best experience, a Mac or Linux environment is preferred. In addition we'll need the following software pre-installed.

- [Git](http://git-scm.com/downloads) or "brew install git"	
- A [GitHub](https://github.com) account
- [**optional**] Java, Your favorite Java editor (Eclipse, IntelliJ IDEA, Netbeans) or your favorite language IDE if you want to build/package artifacts. Installable artifacts will be provided if you do not want to build.
- [The stackato CLI] (http://www.activestate.com/stackato/download_client) - download the latest version that is appropriate for your laptop and follow the instructions in README.txt. 
- Create an alias for stackato as cf. You can create an alias for ```stackato``` as ```cf``` in which case the stackato CLI commands will be approximately similar to the cf CLI commands

Verify that you're using the right command with any of the following commands.

```
cf --version
```

You should see an output like below.

`stackato 3.2.1 (3.2.1 @ 2015-04-10 14:28:15 -0700)`

or

```
cf --help
```

##Recommended Exercises - User Related

It is recommended that you run through these exercises sequentially since they are progressive with some dependencies. Each exercise should take about 5-10 mins. to complete.

- Exercise 1: [Target the Cloud Foundry Instance](ex1)
- Exercise 2: [Push your application] (ex2)
- Exercise 3: [More CLI commands and manifest.yml] (ex3)
- Exercise 4: [Connect to a service] (ex4)
- Exercise 5: [Scale your application] (ex5)
- Exercise 6: [Health Monitoring] (ex6)
- Exercise 7: [Draining logs] (ex7)
- Exercise 8: [Blue/Green Deploy] (ex8)
- Exercise 9: [Jenkins integration] (ex9)

##Recommended Exercises - Admin Related

- Exercise 1: [Quotas] (exa1)
- Exercise 2: [Security Groups] (exa2)
- Exercise 3: [Create a Service Broker] (exa3)

##Optional Exercises

These exercises are optional. Try them if you have some time to spare!

##More Resources

##Contact







