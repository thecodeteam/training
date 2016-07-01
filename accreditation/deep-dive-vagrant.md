# Deep Dive: Vagrant
### 2016 Q3 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

![fit](http://upload.wikimedia.org/wikipedia/commons/8/87/Vagrant.png)

---

# Recap: Vagrant

Create and configure lightweight, reproducible, and portable development environments.

Boot up entire configured systems in minutes.

Run them anywhere!

---

# Basic Vagrantfile

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
end
```

---

# Vagrant boxes

Many to choose from, have a look at http://vagrantbox.es
 - CentOS
 - SLES
 - Debian/Ubuntu
 - FreeBSD
 - Arch
 - Windows!

---

# Windows on Vagrant

Officially supported images can be found at
https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/

![inline](images/vagrant-windows.png)

---

# Create a new Vagrant environment

Add a new Vagrant box

```
  vagrant box add win8.1 http://aka.ms/vagrant-win81-ie11
```

Initialize and run a new Vagrant environment

```
  vagrant init win8.1
```

```
  vagrant up
```

---

# Demo!

---

# Synced folders

By default, `/vagrant` in the VM is the base directory where your `Vagrantfile` is

```
$ vagrant up
...
$ vagrant ssh
...
vagrant@precise64:~$ ls /vagrant
Vagrantfile
script.sh
README.md
```

---

# Be careful with synced folders!

If you remove something from `/vagrant`, it's deleted in your base directory as well

```
vagrant@precise64:~$ ls /vagrant
Vagrantfile
script.sh
README.md
vagrant@precise64:~$ rm /vagrant/Vagrantfile
vagrant@precise64:~$ exit
$ ls
script.sh
README.md
```


---

# Install and configure apps/services

There are multiple ways of installing apps and services in your Vagrant VMs

 - Scripts (bash, PowerShell)
 - Ansible
 - Puppet
 - Chef
 - etc

---

# Example of bash scripting - 1

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision "shell",
    inline: "apt-get install apache2 -y"
end
```

---

# Example of bash scripting - 2

install-apache.sh:

```
#!/bin/bash
apt-get install apache2 -y
echo "<h1>Hello from Vagrant</h1>" > /var/www/index.html
```
Vagrantfile:

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "install-apache.sh"
end
```

---

# Demo!

---

# Port forwarding

Forward localhost:8080 to vm:80, so we can access services

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "install-apache.sh"
  config.vm.network :forwarded_port, guest: 80, host: 8080
end
```

---

# Multiple VMs

```
Vagrant.configure("2") do |config|
  config.vm.define "web" do |web|
    web.vm.box = "hashicorp/precise64"
    web.vm.provision :shell, path: "install-apache.sh"
    web.vm.network :forwarded_port, guest: 80, host: 8080
  end

  config.vm.define "db" do |db|
    db.vm.box = "hashicorp/precise64"
    db.vm.provision :shell, path: "install-mysql.sh"
    db.vm.network :forwarded_port, guest: 3306, host: 33306
  end
end

```

---

# Connecting to multiple VM setups

```
$vagrant ssh web
...
vagrant@web:~$
```

```
$vagrant ssh db
...
vagrant@db:~$
```

---

# Customize the VMs

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.provision :shell, path: "install-apache.sh"
  config.vm.network :forwarded_port, guest: 80, host: 8080

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end
end
```

---

# Demo!

---

# Summary

 - Use Vagrant to easily set up test environments
 - Share your Vagrantfiles and scripts so anyone can use them
 - Create your own demos!

---

# For more information

http://vagrantup.com

http://vagrantbox.es

http://github.com/emccode/vagrant
