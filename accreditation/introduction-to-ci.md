autoscale: true
# Introduction to Continuous Integration

---

## The Problem:

* Rapid Change -> Rapid Business Value

but...

* Rapid Change -> Lack of Confidence (maybe)

---

![fit](http://s2.quickmeme.com/img/e0/e07b5437703f88eb4229adc1c6931061d4c5557f761c048dac3d12f9b8e4846a.jpg)

---

![fit](http://cdn.memegenerator.net/instances/400x/24722869.jpg)

---

## How is this solved traditionally?

* Intermittent 'Integration'
* Slow release train
* Manual QA Testing
* Manual Performance Testing
* 'Release Meetings'

![inline](http://vignette1.wikia.nocookie.net/starpolar/images/6/6b/Notime.jpg/revision/latest?cb=20150225125846)

---

## How do we solve this *now*?

---

#Continous Integration

---

## The Flow

---

#Stage 1


* Developer makes changes locally, tests locally
  * Developer runs local unit tests
  * (optional) Developer runs manual integration tests using CI system

---

#Stage 2  

* Developer checks in the code (`git`, `subversion`)
* CI system begins testing
  * Spins up resources required for test (VMs, containers, etc)
  * Checks out code revision added by developer
  * Runs series of full tests against database, other services, etc, as needed.

--- 

#Stage 3

* Results of test returned to developer (usually 10-60 minutes)
* Checkin either rejected (failed test) or accepted (passed test)

---

> this is a change in mindset first - tools second.

---

# The Tools

* Jenkins (http://jenkins-ci.org/) (opensource)
* ConcourseCI (http://concourse.ci) (OSS, from CloudFoundry)
* TeamCity (https://www.jetbrains.com/teamcity/)
* Travis (https://travis-ci.org/) (hosted)
* Codeship (https://codeship.com/) (hosted)
* Shipptable (http://www.shippable.com/) (hosted)
* CruiseControl (http://cruisecontrol.sourceforge.net/)
* CircleCI (https://circleci.com/features) (hosted)

---

# A Look at Travis