# DevOps tools: Vagrant and Packer
### 2015 Q3 EMC Accreditation
### Jonas Rosland (@jonasrosland) &
### Matt Cowger (@mcowger)

---

# Hashicorp

![fit](https://pbs.twimg.com/profile_images/525656622308143104/0pPm3Eov.png)

---

# Hashicorp

Founded in 2012

Creates Open Source software like:
 - Vagrant
 - Packer
 - Serf
 - Consul
 - Terraform
 - Vault

---

![fit](http://upload.wikimedia.org/wikipedia/commons/8/87/Vagrant.png)

---

# Vagrant

Create and configure lightweight, reproducible, and portable development environments.

Boot up entire configured systems in minutes.

Run them anywhere!

---

# Vagrant will change how you work

Install Vagrant on Windows, OS X or Linux

Create a single file to describe the type of machine you want

Run a single command

---

# Vagrantfile

```
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
end
```

---

# Run Vagrant

```
vagrant up
```

---

# Demo!

---

# Three-node ScaleIO cluster demo!

```
git clone https://github.com/jonasrosland/vagrant-scaleio
cd vagrant-scaleio
vagrant up
```

---

![fit](https://d23f6h5jpj26xu.cloudfront.net/mitchellh_24702982422030_small.png)

---

# Packer

### A tool for creating identical machine images for multiple platforms from a single source configuration

---

# Packer

Packer is easy to use and automates the creation of any type of machine image

Embraces modern configuration management

Encouraging you to use automated scripts to install and configure everything

Packer brings machine images into the modern age, unlocking untapped potential and opening new opportunities

![right,50%](https://packer.io/assets/images/screenshots/vmware_and_virtualbox-bdcc1aa6.png)

---

# Packer images

Build images for Amazon EC2, DigitalOcean, Google Compute Engine, QEMU, VirtualBox, VMware, and more

Support for more platforms is on the way, and anyone can add new platforms via plugins

![right,130%](https://packer.io/assets/images/screenshots/works_with-a1a499d3.png)

---

# Packer benefits

Use it in a continuous delivery pipeline

Parity between dev and prod - all images are the same

Create demos and appliances

---

# For more information

haschicorp.com

vagrantup.com

packer.io
