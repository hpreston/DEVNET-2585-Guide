import requests

url = "http://127.0.0.1:2224/restconf/api/running/interfaces/interface/GigabitEthernet1"

querystring = {"deep":""}

payload = "{\n  \"ietf-interfaces:interface\": {\n    \"name\": \"GigabitEthernet1\",\n    \"description\": \"**THIS IS INTERFACE 1** ** DO NOT CHANGE UNDER PENALTY OF DEATH**\",\n    \"type\": \"iana-if-type:ethernetCsmacd\",\n    \"enabled\": true,\n    \"ietf-ip:ipv4\": {\n    },\n    \"ietf-ip:ipv6\": {\n    }\n  }\n}"
headers = {
    'authorization': "Basic dmFncmFudDp2YWdyYW50",
    'accept': "application/vnd.yang.data+json",
    'content-type': "application/vnd.yang.data+json",
    'cache-control': "no-cache",
    'postman-token': "32285eeb-6d5d-1172-3770-6adf2bb81e7e"
    }

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

print(response.text)
