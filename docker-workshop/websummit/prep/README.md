3-Hour Docker Workshop Training Prep
====================================

Using [Docker Machine with the experimental EMC {code} extension framework](http://blog.emccode.com/2015/09/26/make-docker-machine-do-anything-with-our-experimental-extensions/) deploy a host. Each student needs 2 hosts.

#### For US-East-1 (private AMI using Ubuntu 14.04.03 with Kernel 3.19-30)
```
$ docker-machine -D create --driver amazonec2 --amazonec2-access-key <access-key> --amazonec2-secret-key <secret-key> --amazonec2-vpc-id <vpc-id> --amazonec2-zone "b" --amazonec2-ami ami-f6e6979c --engine-install-url "https://get.docker.com" --extension /Users/kcoleman/Desktop/student.json student001a

$ docker-machine -D create --driver amazonec2 --amazonec2-access-key <access-key> --amazonec2-secret-key <secret-key> --amazonec2-vpc-id <vpc-id> --amazonec2-zone "b" --amazonec2-ami ami-f6e6979c --engine-install-url "https://get.docker.com" --extension /Users/kcoleman/Desktop/student.json student001b
```

#### For EU-West-1 (private AMI using Ubuntu 14.04.03 with Kernel 3.19-30)
```
$ docker-machine -D create --driver amazonec2 --amazonec2-access-key <access-key> --amazonec2-secret-key <secret-key> --amazonec2-region "eu-west-1" --amazonec2-ami ami-0ab16e79 --amazonec2-vpc-id <vpc-id> --engine-install-url "https://test.docker.com" --extension /Users/kcoleman/Desktop/student.json student001a

$ docker-machine -D create --driver amazonec2 --amazonec2-access-key <access-key> --amazonec2-secret-key <secret-key> --amazonec2-region "eu-west-1" --amazonec2-ami ami-0ab16e79 --amazonec2-vpc-id <vpc-id> --engine-install-url "https://test.docker.com" --extension /Users/kcoleman/Desktop/student.json student001b
```
