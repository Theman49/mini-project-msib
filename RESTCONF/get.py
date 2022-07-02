import requests as req
import json
req.packages.urllib3.disable_warnings()


api_url = "https://10.10.20.200/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept" : "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

auth = ("admin", "Admin12345")

res = req.get(api_url, auth=auth, headers=headers, verify=False)

print(res.text)
