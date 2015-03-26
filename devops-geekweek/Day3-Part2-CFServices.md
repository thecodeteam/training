# DevOps Agile Geek Week
## Day 3

^ Open this presentation with [Deckset](http://www.decksetapp.com/)
^ Jonas

---

#Cloud Foundry Services

---

* Applications don't exist in a vacuum
  * Databases
  * Messages Busses
  * Caching Layers
  * Storage Systems

---

# some examples:

* redis, mongodb, riak, postgresql
* 0mq, rabbitMQ, redis
* redis, memcached
* s3, swift, atmos

---

  > How do we manage this without hardcoding and manual effort?

---

# Service bindings

1. Create a service (from market place, or internal)
  * `cf create-service`
  * system automatically requests new service instance from service broker
  * broker responds with connection information
2. Bind service to application:
  * `cf bind-service`
3. Application gets credentials via `VCAP_SERVICES` environment variable
4. Application connects to service

---

* multiple apps can be bound to same service (think databases, or message buses)
* service brokers are easy to write
* all instances of app all treated equally
