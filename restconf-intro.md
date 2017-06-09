# DEVNET-2585 - Hands On Kicking the Tires of RESTCONF

###Table of Contents
- [Initial Workstation Prep](DEVNET-2585-Guide.md)
- [A Brief Introduction to RESTCONF](restconf-intro.md)
- [Building the RESTCONF URI](restconf-lab.md)
- [Using POSTMAN to Send RESTCONF](postman-lab.md)
- [Conclusion](conclusion.md)
- [Lab Clean Up](cleanup.md)


# RESTCONF

> an HTTP-based protocol that provides a programmatic interface for accessing data defined in YANG, using the datastore concepts defined in the Network Configuration Protocol (NETCONF). 
> 
> [RFC 8040](https://tools.ietf.org/html/rfc8040)

As powerful and great an improvement over SNMP that NETCONF is, there are many that desire a REST API interface for network devices.  Rather than develop an entirely new protocol and data model, the IETF has extended NETCONF into RESTCONF.  

## RESTCONF Details

* [RFC 8040](https://tools.ietf.org/html/rfc8040) - January 2017
* Uses HTTP(S) for transport
* Tightly coupled to the YANG data model definitions 
* Provides JSON or XML data formats

## So, no more NETCONF then?  

RESTCONF is **NOT** a replacement for NETCONF.  RESTCONF provides an API that aligns with other Web Application APIs to provide an easy entry point for developers.  Though the gaps maybe eventually be filled, today RESTCONF lacks complete feature parity with NETCONF.   

![](assets/std_net_mgmt_options.jpg)

More likely we will see both NETCONF and RESTCONF leveraged simultaneously by different clients.  

### NOTE: RESTCONF draft Support

*As RESTCONF was fully standardized in January 2017, many vendor implementations of the technology were done based on "drafts", and are currently being updated to full standard support.  Beginning with IOS-XE version 16.3, "draft support" for RESTCONF has been included, and is leveraged within this lab.  An upcoming release of IOS-XE will provide full standard support, and this lab will be updated at that time.*
![](assets/restconf_protocol_stack1.jpg)

## Transport - HTTP

Like other REST APIs, RESTCONF leverages the HTTP protocol to encapsulate and send messages.  Authentication is accomplished using typical HTTP Authentication models such as Basic Authentication where usernames and passwords are encoded in BASE64 and transmitted in a Header.

## Operations - HTTP CRUD

REST APIs typically implement CRUD (Create, Retrieve, Update, and Delete) operations leveraging HTTP available methods.  RESTCONF maps the NETCONF operations into these HTTP methods as shown in this table.  

|  RESTCONF   | NETCONF  | 
|  ---  |  --- |
| GET | `<get>`, `<get-config>` | 
| POST | `<edit-config>` (operation="create") |
| PUT | `<edit-config>` (operation="create/replace") |
| PATCH | `<edit-config>` (operation="merge") |
| DELETE | `<edit-config>` (operation="delete") |

## Content - XML or JSON

One of the major advantages RESTCONF has over NETCONF is its ability to leverage JSON as a data format.  Many developers prefer JSON over XML due to easier readability and lower overhead.  

When crafting a RESTCONF request, you must specify the data format being sent, and requested by the Agent.  This is done in the typical HTTP way, using request headers.  

* **Content-Type**: Specify the type of data being sent from the client
* **Accept**: Specify the type of data being requested by the client

RESTCONF describes the following MIME types to be used in these headers to indicate the format being requested.  

* **application/vnd.yang.data+json**
* **application/vnd.yang.data+xml**


### Continue - [Building the RESTCONF URI](restconf-lab.md)