import requests

url = "http://127.0.0.1:2224/restconf/api/running/interfaces/interface/GigabitEthernet3"

querystring = {"deep":""}

payload = "{\n  \"ietf-interfaces:interface\": {\n    \"name\": \"GigabitEthernet3\",\n    \"description\": \"**THIS IS INTERFACE 3\",\n    \"type\": \"iana-if-type:ethernetCsmacd\",\n    \"enabled\": true,\n    \"ietf-ip:ipv4\": {\n      \"address\": [\n        {\n          \"ip\": \"192.168.185.1\",\n          \"netmask\": \"255.255.255.0\"\n        }\n      ]\n    },\n    \"ietf-ip:ipv6\": {\n    }\n  }\n}\n"
headers = {
    'authorization': "Basic dmFncmFudDp2YWdyYW50",
    'accept': "application/vnd.yang.data+json",
    'content-type': "application/vnd.yang.data+json",
    'cache-control': "no-cache",
    'postman-token': "bea85d52-4b04-5295-6bd4-5e586879cc00"
    }

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

print(response.text)
