# DEVNET-2585 - Hands on Kicking the Tires of RESTCONF

### Table of Contents
- [Introduction](DEVNET-2585-Intro.md)
- [Module 1 - Exploring the YANG Data Model](DEVNET-2585-M1.md)
- [Module 2 - Building the RESTCONF URI](DEVNET-2585-M2.md)
- [Module 3 - Using POSTMAN to Send RESTCONF](DEVNET-2585-M3.md)
- [Module 4 - Using Python to Send RESTCONF](DEVNET-2585-M4.md)
- [Closing](DEVNET-2585-Close.md)

### Objectives


1. View the Contents of a YANG Model
2. Using pyang Open and View a YANG Model
3. Retrieve YANG Data From a Router



## Module 1.1 - View the Contents of a YANG Model

While we do not cover YANG in detail it's important to understand what a YANG model and what the data structure looks like.

**From the terminal window please enter the following:**

```
cd ~/DEVNET-2585-Guide/code
```

Now let's use `more` to view the contents of the ietf-interfaces YANG model. 

**From the terminal window please enter the following:**

```
more ietf-interfaces.yang
```

As you scroll through the contents of the file you will notice a highly detailed description of this particular YANG model. While the details are valuable to an engineer wishing to work with the particular model it's not conducive to viewing the data structure.




## Module 1.2 - Using pyang to View an IETF YANG Model

In this module we will use the Python library `pyang` to view the data structure used by the ietf-interfaces YANG model.  After running the command we will briefly discuss important aspects of the model including containers, lists and a leaf.

**From the terminal window please enter the following:**

```
pyang -f tree ietf-interfaces.yang
```

You should see an output similar to the shaded box below.

```
module: ietf-interfaces
    +--rw interfaces
    |  +--rw interface* [name]
    |     +--rw name                        string
    |     +--rw description?                string
    |     +--rw type                        identityref
    |     +--rw enabled?                    boolean
    |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
    +--ro interfaces-state
       +--ro interface* [name]
          +--ro name               string
          +--ro type               identityref
          +--ro admin-status       enumeration {if-mib}?
          +--ro oper-status        enumeration

<<<OUTPUT TRUNCATED>>>

```
The first thing you should notice is the lack of data. Remember we are only viewing the YANG model. Not the data contained on a device. That comes later. In this case there are a couple of details we need to be aware of.

- `module: ietf-interfaces` - This line states the specific YANG model we are currently viewing.
- `rw interfaces` and `ro interfaces-state` - These entries are a `container` which represents of a node of data.
	-  The other point of interest is the `[name]` field call a `key`. A key represents a unique data node. If you happen to query a router with three interfaces it would report back 3 instances of the `re interface` name with the specific interface listed.
-  Under the individual keyed interfaces are leaf values. An example is `rw name` or `rw enabled?`. These represent a single instance of data. Of note:
	-  A leaf is proceeded by either `rw` or `ro` representing a leaf as read-write or read-only.
	-  A leaf with a `?` in the description such as `rw enabled?` means the leaf if optional. All other leaves are mandatory.
	-  The details to the right of the key is the `data type`

	
## Module 1.3 - Using pyang to View a Cisco YANG Model

One of the advantages of YANG is any one can write their own model provided they follow the format as laid out above. This allows vendors to create their own YANG models to address additional data on their platforms. In this example we will use pyang to view one of Cisco's models. What should be clear short of the model name the format doesn't change.

**From the terminal window please enter the following:**

```
pyang -f tree cisco-platform-software.yang
```

You should see an output similar to the shaded box below:

```
module: cisco-platform-software
    +--ro platform-software-status-control-process
    |  +--ro control-process* [name]
    |     +--ro name                  string
    |     +--ro status?               string
    |     +--ro updated?              uint8
    |     +--ro load-average-stats
    |     |  +--ro load-average-status?   string
    |     |  +--ro minutes* [number]
    |     |     +--ro number     uint8
    |     |     +--ro average?   decimal64
    |     |     +--ro status
    |     |        +--ro condition?          string
    |     |        +--ro threshold-status?   string
    |     |        +--ro threshold-value?    decimal64
    |     +--ro memory-stats
    |     |  +--ro memory-status?       string
    |     |  +--ro total?               uint32
    |     |  +--ro used-number?         uint32

<<<OUTPUT TRUNCATED>>>

```
Before we move on to the next section feel free to look at the other included YANG modules included. Should you want to explore additional YANG models after the lab they are published here: [https://github.com/YangModels/yang](https://github.com/YangModels/yang).

### [Continue to Module 2](DEVNET-2585-M2.md) - Building the RESTCONF URI