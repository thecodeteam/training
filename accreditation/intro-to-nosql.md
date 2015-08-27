# NoSQL
### 2015 Q4 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

---

# "Not Only" SQL

---

# Why Not?

---

* RDBMS Can Do Everything, Right?
  * Transactions, performance...
* Not Quite

---

RDBMs Are Good At:

* SQL (common interface)
* Industry Support
* Small Scale

---

RDBMs Are Bad At:
* Simpler Notation
* Ultra Low Latency
* Large Scale (>10 nodes)
* Changes (schema, etc) on the fly


---

#Lets Use the Right Tool for the Right Job

---

NoSQL Are Good At:

* Simple Notation / Access
* Low Latency
* Large Scale
* Changes
  * With great power comes great responsibility

![inline](https://btglifestyle.files.wordpress.com/2013/06/uncle-ben-from-spiderman.jpg)

---

NoSQL (Might Be) Bad At:

* Transactional Consistency
* SQL (JOINs, etc)
* Off the Shelf Application Support

---

# Examples of SQL:

* Oracle
* MySQL
  * careful!
* Postgres
* MSSQL Server


---

# CAP Theorem

![inline](http://i.imgur.com/JNN7Ucs.png)

---

#4 Common Types

---

#Key Value

* Stores a simple value (10,456,345) in a 'key': ("usercount")
* Simple 'CRUD' semantics
  * Create, Read, Update, Delete
* No schema at all, generally
* Stunningly Scalable (hundreds->thousands of nodes)
* "Get me the current MacOS user count"
* XtremSF cards

---

* Examples:
  * Redis (http://try.redis.io/)
  * Memcached
  * Aerospike
  * Cassandra
  * Basho Riak
  * LevelDB
  * Couchbase

---

# Document Stores

* Store Larger Scale Documents
  * Usually in standard encoding: `JSON`, `YML`, `BSON`
  * *not* Word documents

---

```javascript
{
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}

```

---
  
* Retrieve Documents Based on Key *or* Contents
* Highly Scalable (tens to hundreds of nodes)
* "Show me documents that talk about MacOS"
* ScaleIO

---

* Examples:
  * CouchDB / Cloudant (try it for free: https://cloudant.com/sign-up/)
  * MarkLogic (popular in .gov)
  * MongoDB (try it for free: https://mongolab.com/)
  * Amazon SimpleDB (outdated)
  * BaseX

---

# Graph Database

* Represents connections between objects (nodes):
* For instance, if "Wikipedia" were one of the nodes, one might have it tied to properties such as "website", "reference material", or "word that starts with the letter 'w'"
* For associating simple data types, these tend to be orders of magnitude faster than SQL
* "Show me everyone that likes MacOS"
* Rough Scene :)

^ Twitter finding friends
^ Logistics shortest route

---


![inline](http://i.imgur.com/4xzfVMi.png)

* Examples:
  * Neo4j (http://console.neo4j.org/)
  * InfiniteGraph
  * AllegroGraph
  * BlazeGraph (used in ViPR SRM)

---

# (Wide) Column Store

* Uses tables, rows, columns, but does not fix schema like SQL (because its focused on storing the columns, not the rows)
* Great for computing aggregates of huge amounts of data (common in Big Data, data warehouse)
* "Show me everyone that clicked this link between yesterday and today, sorted by age"
  * Where total clicks is tens of millions
* Isilon, ScaleIO, DCA

---

* Examples:
  * HBase (Hadoop)
  * Greenplum
  * Vertica
  * Teradata
  * Amazon Redshift (https://aws.amazon.com/redshift/)
  * Google BigQuery


---

#Conclusions

* Lots of different options
  * Let your data dictate management method
* SQL is not always the right choice
* Try them!
