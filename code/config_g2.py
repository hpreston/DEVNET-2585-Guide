import requests

url = "https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "**THIS IS INTERFACE 2",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.20.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

headers = {
    'accept': "application/yang-data+json",
    'content-type': "application/yang-data+json",
    }

response = requests.put(url,
                        auth = ("vagrant", "vagrant"),
                        headers=headers,
                        json=payload,
                        verify=False)

print(response.text)
