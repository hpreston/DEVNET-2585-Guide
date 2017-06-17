# DEVNET-2585 - Hands on Kicking the Tires of RESTCONF

### Table of Contents
- [Introduction](DEVNET-2585-Intro.md)
- [Module 1 - Exploring the YANG Data Model](DEVNET-2585-M1.md)
- [Module 2 - Building the RESTCONF URI](DEVNET-2585-M2.md)
- [Module 3 - Using POSTMAN to Send RESTCONF](DEVNET-2585-M3.md)
- [Module 4 - Using Python to Send RESTCONF](DEVNET-2585-M4.md)
- [Closing](DEVNET-2585-Close.md)




## Document Conventions

The most important convention in the lab guide is the use of the `grey box`. It's either used to draw your attention or to call out something that should be directly entered into the terminal.

To draw a distinction as to when you should just view the output vs. actually enter something into the terminal I will prompt any time you should type with

**From the terminal window please enter the following:**
```
enter this into the terminal
```

The intention is to directly past that content into the terminal. Free free to type if you'd prefer.

## Initial Workstation Prep

First let's make sure we are in our home directory:

**From the terminal window please enter the following:**

```
cd ~
```

Now let's clone our Git repo for the lab.

**From the terminal window please enter the following:**

```
git clone https://github.com/brybyrne/DEVNET-2585-Guide.git
```

Once the repo has downloaded let's get into our directory and run the start-up script.

**From the terminal window please enter the following:**

```
cd DEVNET-2585-Guide

source ./startup.sh
```

At the completion of the script you should be faced with a command prompt of:

```
(venv)$
```

Let's start the lab!


### [Continue to Module 1](DEVNET-2585-M1.md) - Exploring the YANG Data Model