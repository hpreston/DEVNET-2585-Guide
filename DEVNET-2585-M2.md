# DEVNET-2585 - Hands on Kicking the Tires of RESTCONF

### Table of Contents
- [Introduction](DEVNET-2585-Intro.md)
- [Module 1 - Exploring the YANG Data Model](DEVNET-2585-M1.md)
- [Module 2 - Building the RESTCONF URI](DEVNET-2585-M2.md)
- [Module 3 - Using POSTMAN to Send RESTCONF](DEVNET-2585-M3.md)
- [Module 4 - Using Python to Send RESTCONF](DEVNET-2585-M4.md)
- [Closing](DEVNET-2585-Close.md)

### Objectives
1. Understand the basics of the RESTCONF Protocol.
2. Understand the relationship of RESTCONF and YANG in building the API calls.
3. Understand the basics of making RESTCONF API calls to retrieve and update device configuration.


One aspect true of all REST APIs is the importance of the URI in identifying the data being requested or configured, and RESTCONF is no exception. One thing unique about RESTCONF is that it lacks any true "API Documentation" that a developer would use to learn about leveraging it. Rather, the YANG Models themselves ARE the API documentation.


## Module 2.1 - Building the RESTCONF URI


In this section we will walk through creating a REST API using `curl` call to our lab router. Curl is a tool to transfer data from, or to, a server using among other protocols HTTP/HTTPS.

Before we begin let's briefly review the RESTCONF URI format.

**The RESTCONF URI format**
```
https://<ADDRESS>/<ROOT>/<DATA STORE>/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>]
```
Some notes:

* **ADDRESS** - Of the RESTCONF Agent
* **ROOT** - The main entry point for RESTCONF requests.
	* Discoverable at https://<ADDRESS>/.well-known/host-meta
* **DATA STORE** - The data store being queried 
* **[YANG MODULE:]CONTAINER** - The base model container being used.  Providing the module name is optional.
* **LEAF** - An individual element from within the container
* **[?&#60;OPTIONS&#62;]** - optional parameters that impact returned results.


Now that we have reviewed the format of our URL let's start building API calls with curl.

**From the terminal window please enter the following:**

```
curl -k -u vagrant:vagrant \
    -H "Accept: application/yang-data+json" \
   https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces
```

Before we review the output let's talk through the command.

- First we are using the `\` command to break the command into a multiple lines for easier reading
- `-k` Allows "insecure" requests with self-signed certificates
- In the first line the `-u vagrant:vagrant` specifies the username and password of of the lab router
- In the second line the `-H` specifies the HTTP headers we will send in our in our request. We are telling the router we expect JSON as our data format.
- The third line is the actual REST URI. Recall that in our lab we are running a router in a virtual machine. The local hypervisor is remapping port 443 to 2225. In a 'real' environment the URL would typically not re-map port 443.

If we sent our curl command correctly we should see similar output to:

```
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "description": "**THIS IS INTERFACE 1** ** DO NOT CHANGE UNDER PENALTY OF DEATH**",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet2",
        "description": "**THIS IS INTERFACE 2",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.20.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet3",
        "description": "**THIS IS INTERFACE 3",
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
    ]
  }
}
```

<!--
This section isn't as relevant in RFC8040.  Option is now `depth=NUM` to detail how many layers of nesting to return.  Default is "unbound" which returns everything.  

## Module 2.2 - Using Options to Gather Additional Details

In the previous example we used curl to request the interfaces running on a router. This example wasn't overly useful as it didn't contain any actual details on the configuration of the interface. Let's modify our curl request using some of the options in our URI. We can append one of the following:

- ?deep
- ?shallow
- ?verbose

**From the terminal window please enter the following:**

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

Of particular interest in the `?verbose` option. The response output passes back additional details to build our REST calls for the individual interfaces.

Response of `?verbose` call.

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
Let's try our CURL command one more time to pull configuration details of interface Gigabit 3. In this example we will just append `/GigabitEthernet3?deep` to the end of our first curl command.

**From the terminal window please enter the following:**

```
curl -u vagrant:vagrant \
    -H "Accept: application/vnd.yang.data+json" \
   http://127.0.0.1:2224/restconf/api/running/interfaces/interface/GigabitEthernet3?deep
```

The output should match below:

```
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet3",
    "description": "**THIS IS INTERFACE 3",
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
``` -->

## Module 2.3 - Viewing Operational Data

For this example we will craft our REST call to pull interface statistics from the `operational` data store.

**From the terminal window please enter the following:**

```
curl -k -u vagrant:vagrant \
   -H "Accept: application/yang-data+json" \
	 https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces-state/interface=GigabitEthernet3
```   

Before we look at the output let's review a couple of changes:

- Additionally we are no longer calling the `interface` container in the ietf-intefaces YANG model. We are now using the 2nd container `interface-state`. Feel free to review by sending `pyang -f tree ietf-interfaces.yang`

After running the command the output should look similar to:

```
{
  "ietf-interfaces:interfaces-state": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "type": "iana-if-type:ethernetCsmacd",
        "admin-status": "up",
        "oper-status": "up",
        "last-change": "2017-06-17T12:00:02.000776+00:00",
        "if-index": 0,
        "phys-address": "08:00:27:21:c9:9f",
        "speed": 1024000000,
        "statistics": {
          "discontinuity-time": "2017-06-17T11:57:46.00028+00:00",
          "in-octets": 127099,
          "in-unicast-pkts": 876,
          "in-broadcast-pkts": 0,
          "in-multicast-pkts": 0,
          "in-discards": 0,
          "in-errors": 0,
          "in-unknown-protos": 0,
          "out-octets": 92682,
          "out-unicast-pkts": 635,
          "out-broadcast-pkts": 0,
          "out-multicast-pkts": 0,
          "out-discards": 0,
          "out-errors": 0
        }
      },
      <<OUTPUT TRUNCATED>>
    }
```

### [Continue to Module 3](DEVNET-2585-M3.md) - Using Postman to Send RESTCONF
