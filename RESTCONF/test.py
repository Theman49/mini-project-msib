import requests
import json
requests.packages.urllib3.disable_warnings()

payload = json.dumps({
  "dhcp": {
      "Cisco-IOS-XE-dhcp:pool": [
          {
              "id": "subnet1",
              "default-router": {
                  "default-router-list": [
                      "192.168.0.1"
                  ]
              },
              "network": {
                  "primary-network": {
                      "number": "192.168.0.0",
                      "mask": "255.255.255.192"
                  }
              }
          },
          {
              "id": "subnet2",
              "default-router": {
                  "default-router-list": [
                      "192.168.0.65"
                  ]
              },
              "network": {
                  "primary-network": {
                      "number": "192.168.0.64",
                      "mask": "255.255.255.224"
                  }
              }
          }
      ]
  }
})
headers = {
'Accept': 'application/yang-data+json',
'Content-Type': 'application/yang-data+json'
}

auth = ('admin', 'Admin12345')
url = 'https://10.10.20.200/restconf/data/Cisco-IOS-XE-native:native/ip/dhcp'
response = requests.put(url, auth=auth, headers=headers, data=payload, verify=False)

print(response)