import requests

url = "http://127.0.0.1:2224/restconf/api/running/interfaces/interface/GigabitEthernet2"

querystring = {"deep":""}

payload = "{\n  \"ietf-interfaces:interface\": {\n    \"name\": \"GigabitEthernet2\",\n    \"description\": \"**THIS IS INTERFACE 2\",\n    \"type\": \"iana-if-type:ethernetCsmacd\",\n    \"enabled\": true,\n    \"ietf-ip:ipv4\": {\n      \"address\": [\n        {\n          \"ip\": \"172.16.20.1\",\n          \"netmask\": \"255.255.255.0\"\n        }\n      ]\n    },\n    \"ietf-ip:ipv6\": {\n    }\n  }\n}\n"
headers = {
    'authorization': "Basic dmFncmFudDp2YWdyYW50",
    'accept': "application/vnd.yang.data+json",
    'content-type': "application/vnd.yang.data+json",
    'cache-control': "no-cache",
    'postman-token': "64a80ac3-3e32-0ed4-e8b3-ee9d69f92ca8"
    }

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

print(response.text)
