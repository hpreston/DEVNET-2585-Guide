# DEVNET-2585 - Hands On Kicking the Tires of RESTCONF

###Table of Contents
- [Initial Workstation Prep](DEVNET-2585-Guide.md)
- [A Brief Introduction to RESTCONF](restconf-intro.md)
- [Building the RESTCONF URI](restconf-lab.md)
- [Using POSTMAN to Send RESTCONF](postman-lab.md)
- [Conclusion](conclusion.md)
- [Lab Clean Up](cleanup.md)


The most important convention in the lab guide is the use of the `grey box` A large portion of this lab is designed so you can cut and paste the commands into your terminal to minimize typos. So when you see:

```
text like this
```
The intention is to directly past that content into the terminal. Free free to type if you'd prefer.

Before we can start working through the lab we need to take a few moments to prepare our working environment. I will not assume that all students are familiar with the tools we use today so a brief run down on of the components.

- Not to state the obvious but we are running on MacBooks. For those that aren't familiar with a Mac please let me know. Just a quick tip to copy use `command+c` and to paste use `command+v`
- For the purpose of the lab we will be sending commands to a CSR1000v router running locally on the MacBook running in Virtual Box.
- [Vagrant](http://www.vagrantup.com) is a tool for creating lightweight, reproducible development environments. We will use Vagrant to start our CSR.
- Virtual Environments (virtualenv) are used to create isolated Python 
environments. It solves the need for version dependencies between projects.
- If you are attempting this lab after Cisco Live you will need to install Python3.5 and pip.
- We will leverage [Postman](http://www.getpostman.com) to make RESTCONF calls to the router in our lab.

Let's get into prepping the environment. First let's start by ensuring we are in our home directory. For those not familiar with Linux command structures the `~` character is an alias for the current users home directory.

```
cd ~
```

Now we need to pull down the required scripts and files for the lab. We will clone the git repository and change to the directory it created. Once we change into the directory we will run a list `ls` and we should count 4 files and 2 directories.


```
git clone https://github.com/brybyrne/DEVNET-2585-Guide.git

cd DEVNET-2585-Guide

ls

```
**OPTIONAL**
The default hostname on OSX can be a bit lengthy. If you would like to shorten it enter the following to chagne the hostname to `$`

```
PS1=$
```


Now that we have all the required files let's start up the CSR100V.

```
vagrant up
```
The process to boot the router takes 2-3 minutes. The router will be ready when a large amount of green text fills the terminal screen.

Let's move on and prepare out Python environment. As these are shared laptops for the lab we will be working inside of a virtual environment. In this step we will create the virtual environment and install our Python requirements.

**NOTE** For this step please enter each command and wait for completion rather than pasting all the commands at the same time.

```
virtualenv venv --python=python3.5

source venv/bin/activate 

pip install -r requirements.txt
```
After completion if you enter `python --version` the output should match the following:

```
(venv) $python --version
Python 3.5.2
(venv) $
```
Based on some last minute changes to the lab we will need to manually make a couple of modifications to the router so the lab works. We will make similar modifications over the course of the lab. So we have some basic configuration in please let's jump into our router:

To access the router we use the command

```
vagrant ssh
```

Paste the following in the router:

```
conf t

interface GigabitEthernet 1
 description **THIS IS INTERFACE 1** ** DO NOT CHANGE UNDER PENALTY OF DEATH**

interface GigabitEthernet 3
 description **THIS IS INTERFACE 3**
 ip add 192.168.185.1 255.255.255.0
 no shut
 
 end
 
 copy run start
```

After we have completed the initial router prep let's drop back to the Mac command shell by typing

```
exit
```

Enough with our device prep let's jump into RESTCONF

### Continue - [A Brief Introduction to RESTCONF](restconf-intro.md)
