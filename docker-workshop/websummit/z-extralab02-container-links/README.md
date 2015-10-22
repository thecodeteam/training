Lab III: Connect Docker Containers with Links
===============================

## Description

In this lab you'll learn how to link containers.

### Lab setup

Each of you has been handed a piece of paper with a machine that has Docker and REX-Ray installed. SSH into your machine

#### Mac/Linux
Use Terminal
`$ ssh student@IPADDRESS`

#### Windows
Use PuTTy

## Link an application container to Redis

Continued from [building Redis](https://docs.docker.com/examples/running_redis_service/)

Next we can create a container for our application. We’re going to use the `--link` flag to create a link to the redis container we’ve just created with an alias of `db`. This will create a secure tunnel to the redis container and expose the Redis instance running inside that container to only this container.

`$ docker run --link redis:db -i -t ubuntu:14.04 /bin/bash`

Once inside our freshly created container we need to install Redis to get the redis-cli binary to test our connection.

```
$ sudo apt-get update
$ sudo apt-get install redis-server -y
$ sudo service redis-server stop
```

As we’ve used the `--link redis:db` option, Docker has created some environment variables in our web application container.
```
$ env | grep DB_

# Should return something similar to this with your values
DB_NAME=/violet_wolf/db
DB_PORT_6379_TCP_PORT=6379
DB_PORT=tcp://172.17.0.33:6379
DB_PORT_6379_TCP=tcp://172.17.0.33:6379
DB_PORT_6379_TCP_ADDR=172.17.0.33
DB_PORT_6379_TCP_PROTO=tcp
```

We can see that we’ve got a small list of environment variables prefixed with `DB`. The `DB` comes from the link alias specified when we launched the container. Let’s use the `DB_PORT_6379_TCP_ADDR` variable to connect to our Redis container.
```
$ redis-cli -h $DB_PORT_6379_TCP_ADDR
$ redis 172.17.0.33:6379>
$ redis 172.17.0.33:6379> set docker awesome
OK
$ redis 172.17.0.33:6379> get docker
"awesome"
$ redis 172.17.0.33:6379> exit
```
We could easily use this or other environment variables in our web application to make a connection to our redis container.
