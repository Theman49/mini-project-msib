import requests
import json
requests.packages.urllib3.disable_warnings()

host = ['10.10.20.201', '10.10.20.202']
ip_interfaces = ['172.16.0.2/26', '172.16.0.66/27']
ip_vlan = ['172.16.101.2/26', '172.16.101.66/27']

headers = {
  'Content-Type': 'application/json',
}
auth = ('admin','Admin12345')


for i in range(1, len(ip_interfaces) + 1):
  url = "https://{}/ins".format(host[i-1])
  commands = [
    "vlan 101 ;name prod",
    "interface vlan 101 ;description config by NXAPI prod ;no shutdown ;no ip redirects ;ip address {} ;".format(ip_vlan[i-1]),
    "interface ethernet 1/1 ;description config by NXAPI connect to R{} ;ip address {} ;no shut".format(i, ip_interfaces[i-1]),
    "interface ethernet 1/2 ;description config by NXAPI connect to host ;switchport ;switchport access vlan 101 ;spanning-tree port type edge ;no shutdown ;"
  ]

  for x in range(4):
    payload = json.dumps({
      "ins_api": {
        "version": "1.0",
        "type": "cli_conf",
        "chunk": "0",
        "sid": "1",
        "input": commands[x],
        "output_format": "json"
      }
    })
    response = requests.request("POST", url, auth=auth, headers=headers, data=payload, verify=False)
    print(response.json()['ins_api']['outputs']['output'])

# config interface S2 e1/3
url = "https://{}/ins".format(host[1])
commands = [
"interface ethernet 1/3 ;description config by NXAPI connect to host ;switchport ;switchport access vlan 101 ;spanning-tree port type edge ;no shutdown ;",
"copy run start"
]
for i in range(2):
  payload = json.dumps({
    "ins_api": {
      "version": "1.0",
      "type": "cli_conf",
      "chunk": "0",
      "sid": "1",
      "input": commands[i],
      "output_format": "json"
    }
  })

  response = requests.post(url, auth=auth, headers=headers, data=payload, verify=False)
  print(response.json()['ins_api']['outputs']['output'])