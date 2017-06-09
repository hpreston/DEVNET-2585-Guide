# DEVNET-2585 - Hands On Kicking the Tires of RESTCONF

###Table of Contents
- [Initial Workstation Prep](DEVNET-2585-Guide.md)
- [A Brief Introduction to RESTCONF](restconf-intro.md)
- [Building the RESTCONF URI](restconf-lab.md)
- [Using POSTMAN to Send RESTCONF](postman-lab.md)
- [Conclusion](conclusion.md)
- [Lab Clean Up](cleanup.md)


## Objective

Completion Time: 15 Minutes

* Understand the RESTCONF Protocol, and its basic usage
* Understand the relationship between RESTCONF and YANG Data Models in building API calls
* Understand the basics of making RESTCONF API calls to retrieve and update device configuration

## Building the RESTCONF URIs

One aspect true of all REST APIs is the importance of the URI in identifying the data being requested or configured, and RESTCONF is no exception.  One thing unique about RESTCONF is that it lacks any true "API Documentation" that a developer would use to learn about leveraging it.  Rather, the YANG Models themselves **ARE** the API documentation.  

All RESTCONF URIs follow this format: 

`http://<ADDRESS>/<ROOT>/<DATA STORE>/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>]`

Some notes:

* **ADDRESS** - The IP (or DNS Name) and Port where the RESTCONF Agent is available
* **ROOT** - The main entry point for RESTCONF requests.  
    * Before connecting to a RESTCONF server, you must determine the `root`
    * Per the RESTCONF standard, devices should expose a resource called `/.well-known/host-meta` to enable discovery of `root ` programmatically 
    * However, with many devices still operating on DRAFT RESTCONF specs, this may not be fully implemented. 
    * Device documentation should also specify the `root` path
    * On the Cisco IOS-XE 16.3-16.5, this is `restconf/api`
        * pre-16.3 this was `api`
* **DATA STORE** - The data store being queried 
* **[YANG MODULE:]CONTAINER** - The base model container being used
    * *Inclusion of the module name is optional*
* **LEAF** - An individual element from within the container
* **[?\<OPTIONS>]** - Some network devices may support options sent as query parameters that impact returned results.  
    * These options are **NOT** required and can be omitted 
    * Check device documentation for details on supported parameters 

To make the RESTCONF calls, you can use any client application that supports any REST call.  A common tool is the Chrome Application Postman.  The Linux command line utility "curl" is another great tool for working with REST APIs.  We'll show how to use both in these examples.

## Before We Begin

Please ensure that you are in the correct directory and have prepared the lab environment. 

First validate the directory:
```
pwd
$/Users/XXXXXX/DEVNET-2585-Guide
```

Next confirm that we have our python environment running.

```
which python
$/Users/XXXXX/DEVNET-2585-Guide/venv/bin/python
```
## RESTCONF and the ietf-interfaces

In this first example, we're going to use RESTCONF to investigate the same ietf-interfaces YANG model.  

As we learned, the URI is determined by looking at the underlying YANG model.  Here is a partial ietf-interfaces Model. While we will not be covering YANG in detail during the lab understand that YANG is providing a structured data model used to gather, or change, details on the router. We need to understand the structure of YANG so we can construct our URIs for sending RESTCONF requests.

To view our YANG model use the following commands:

```
pyang -f tree code/ietf-interfaces.yang
```
The output will look similar to the following:

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
          +--ro last-change?       yang:date-and-time
          +--ro if-index           int32 {if-mib}?
          +--ro phys-address?      yang:phys-address
          +--ro higher-layer-if*   interface-state-ref
          +--ro lower-layer-if*    interface-state-ref
          +--ro speed?             yang:gauge64
          +--ro statistics
             +--ro discontinuity-time    yang:date-and-time
             +--ro in-octets?            yang:counter64
             +--ro in-unicast-pkts?      yang:counter64
             +--ro in-broadcast-pkts?    yang:counter64
             +--ro in-multicast-pkts?    yang:counter64
             +--ro in-discards?          yang:counter32
             +--ro in-errors?            yang:counter32
             +--ro in-unknown-protos?    yang:counter32
             +--ro out-octets?           yang:counter64
             +--ro out-unicast-pkts?     yang:counter64
             +--ro out-broadcast-pkts?   yang:counter64
             +--ro out-multicast-pkts?   yang:counter64
             +--ro out-discards?         yang:counter32
             +--ro out-errors?           yang:counter32
```

We will now construct a URI to send to the router. As we saw in the introduction the URI will be constructed in the following format

`http://<ADDRESS>/<ROOT>/<DATA STORE>/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>]`

We can use the built in 'curl' tool to send web request to the router making our RESTCONF call. Let's try it out by requesting a list of interfaces.

Paste the following into your terminal:

```
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces 
```

Before take a look at the output let's review what we just sent to the router

* `-u vagrant:vagrant` provides the credentials for the device
* `-H "Accept: application/vnd.yang.data+json"` sets the HTTP "Accept" header to indicate our preference for JSON data
* We are sending the RESTCONF querry to a virtual router running on the laptop hence using `http://127.0.0.1:2224` in a 'real' environment the request would be sent to the router's IP address on port 80.

The commands hould generate an output similar to:

```
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1"
      },
      {
        "name": "GigabitEthernet2"
      },
      {
        "name": "GigabitEthernet3"
      }
    ]
  }
}
```

Now that we have a response the level of details isn't overly compelling. RESTCONF allows for additional parameters in the URI to modify the data passed back.

We can append one of the following

- ?deep
- ?shallow
- ?verbose

Let's try it out. Feel free to experiment with any of the options below.

```
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces?deep
   
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces?shallow
   
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces?verbose
```

Of particular interest is the `?verbose` option. The response output passes back the URI to access details on the specific interfaces.

Response example:

```
{
  "ietf-interfaces:interfaces": {
    "_self": "/api/running/interfaces",
    "_path": "/if:interfaces",
    "interface": [
      {
        "_self": "/api/running/interfaces/interface/GigabitEthernet1",
        "name": "GigabitEthernet1"
      },
      {
        "_self": "/api/running/interfaces/interface/GigabitEthernet2",
        "name": "GigabitEthernet2"
      },
      {
        "_self": "/api/running/interfaces/interface/GigabitEthernet3",
        "name": "GigabitEthernet3"
      }
    ]
  }
}
```

Based on the output we can now use these details to drill down and pull up specific details on an interface. Let's take a look at interface Gig 3.

```
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces/interface/GigabitEthernet3?deep
```

The response should have passed back interface specific details including the interface description, admin state, and IP address.

```
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet3",
    "description": "**THIS IS INTERFACE 3**",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "192.168.185.1",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {
    }
  }
}
```

Before we move on let's take a quick look at this portion of the URI in bold




Now that we've looked at how to craft the URI for RESTCONF let's look into how we can use tools to make some changes to our router.

http://127.0.0.1:2224/restconf/api/**running**/interfaces/interface/GigabitEthernet3?deep
 
This portion of the URI references data store that contains the particular piece of information we are requesting. In the previous example we were looking for details on the configuration so we used the `running` data store. If we wanted to pull interface statistics we would need to use the `operational` data store. Let's run through an example.

```
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/operational/interfaces-state?deep
```   

There was one additional change in this curl command compared to the other examples. In this case we used a new container from the ietf-interface YANG model. In this example we pulled details form the `interfaces-state` which holds details like packets in/out, collisions, etc. Additionally we can parse the data down even farther by specifying the individual interfaces.

Now that we've seen how to construct a URIs let's look at using some tools to update the router configuration.

### Continue - [Using POSTMAN to Send RESTCONF](postman-lab.md)

