## Agenda

1. Instructor Demo
2. Hands on use by audience
    - use a laptop or browser on your phone

---

## Pre- deployed Mesos Cluster

- A Mesos Master is deployed, and it is also running Zookeeper
    - hostname: TBD:5050
- A Marathon host is deployed
    - hostname: TBD:8080
- A Chronos host is deployed
    - hostname: TBD:4400
- Multiple Mesos slave nodes are deployed
    - Users do not deal with these directly

---

## Instructor Demo

1. Deploy a Python web server using Marathon UI
    - python -m SimpleHTTPServer $PORT
2. Show how to scale the application and halt the application

---

##  Demonstrate use of the Marathon REST API

compose a .json file with this content, on the Marathon host:

```
{
 "id": "web-server-via-rest-api",
 "cmd": "echo 'Hello Mesos fans' > readme-$PORT.txt && python -m SimpleHTTPServer $PORT",
 "mem": 16,
 "cpus": 0.1,
 "instances": 6,
 "constraints": [
   ["hostname", "UNIQUE"]
 ]
}
```

---

## Marathon REST API continued

1. Use curl to call the API

```
curl -i -H 'Content-Type: application/json' -d @test.json localhost:8080/v2/apps
```

---

## Fault detection and recovery Demo

1. Kill an application instance using command line on the agent host running it.
    - ps -aux | grep SimpleHTTPServer
    - kill #
3. Observe Mesos detect this condition and bring the web server back up

---

## Audience Hands On

1. Explore the Marathon GUI, using you laptop, tablet, or phone
2. Install deploy a simple Python web server using the Marathon GUI
    - echo 'phrase of your choice' > yourname && python -m SimpleHTTPServer $PORT
3. Test that your web server is alive at the assigned cluster node / port
4. Scale the application and halt the application

---

## Optional, if time allows

1. Instructor demo of using Chronos UI to deploy a periodically scheduled job.
    - browse to Chronos host:4400
    - create a job
        - name: chronos-sleeper-job
        - command: sleep 40
        - owner: test@test.com
        - schedule: edit to end in PT5M
