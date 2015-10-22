3-Hour Docker Workshop Training Prep
====================================

Using [Docker Machine with the experimental EMC {code} extension framework](http://blog.emccode.com/2015/09/26/make-docker-machine-do-anything-with-our-experimental-extensions/) deploy a host. Each student needs 2 hosts. So run the command twice for each student.

```
$ docker-machine -D create --driver amazonec2 --amazonec2-access-key accesskey --amazonec2-secret-key secreykey --amazonec2-vpc-id vpcid --amazonec2-zone "b" --engine-install-url "https://experimental.docker.com" --extension /Users/kcoleman/Desktop/student.json student001a

$ docker-machine -D create --driver amazonec2 --amazonec2-access-key accesskey --amazonec2-secret-key secreykey --amazonec2-vpc-id vpcid --amazonec2-zone "b" --engine-install-url "https://experimental.docker.com" --extension /Users/kcoleman/Desktop/student.json student001b
```