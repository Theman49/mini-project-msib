import requests
import json
requests.packages.urllib3.disable_warnings()

data_ip = ['172.16.0.1','172.16.0.65']
data_subnet = ['255.255.255.192','255.255.255.224']

host = "10.10.20.200" 
username = "admin"
password = "Admin12345"

headers = {
'Accept': 'application/yang-data+json',
'Content-Type': 'application/yang-data+json'
}

auth = (username, password)

for i in range(2,4):
    url = "https://{}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet{}".format(host, str(i))

    payload = json.dumps({
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet{}".format(str(i)),
        "description": "Configured by RESTCONF subnet {}".format(str(i-1)),
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
        "address": [
            {
            "ip": data_ip[i-2],
            "netmask": data_subnet[i-2] 
            }
        ]
        }
    }
    })

    response = requests.put(url, auth=auth, headers=headers, data=payload, verify=False)

    print(response)

url = "https://{}/restconf/operations/cisco-ia:save-config/".format(host)
resp = requests.post(url, auth=auth, headers=headers, verify=False)
print("save " + resp.text)

'''
payload = json.dumps({
    "dhcp": {
        "Cisco-IOS-XE-dhcp:pool": [
            {
                "id": "subnet1",
                "default-router": {
                    "default-router-list": [
                        "172.16.0.1"
                    ]
                },
                "network": {
                    "primary-network": {
                        "number": "172.16.0.0",
                        "mask": "255.255.255.192"
                    }
                }
            },
            {
                "id": "subnet2",
                "default-router": {
                    "default-router-list": [
                        "172.16.0.65"
                    ]
                },
                "network": {
                    "primary-network": {
                        "number": "172.16.0.64",
                        "mask": "255.255.255.224"
                    }
                }
            }
        ]
    }
})

url = 'https://{}/restconf/data/Cisco-IOS-XE-native:native/ip/dhcp'.format(host)
response = requests.put(url, auth=auth, headers=headers, data=payload, verify=False)

print(response)


payload = json.dumps({
    "router": {
        "Cisco-IOS-XE-ospf:router-ospf": {
            "ospf": {
                "process-id": [
                    {
                        "id": 1,
                        "log-adjacency-changes": False,
                        "network": [
                            {
                                "ip": "172.16.0.0",
                                "wildcard": "0.0.0.255",
                                "area": 0
                            }
                        ]
                    }
                ]
            }
        }
    }
})

url = 'https://{}/restconf/data/Cisco-IOS-XE-native:native/router'.format(host)
response = requests.put(url, auth=auth, headers=headers, data=payload, verify=False)

print(response)
'''