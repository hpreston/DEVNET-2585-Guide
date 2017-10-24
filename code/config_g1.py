import requests

url = "https://127.0.0.1:2225/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "**THIS IS INTERFACE 1** ** DO NOT CHANGE UNDER PENALTY OF DEATH**",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {}
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
