import requests
import json
requests.packages.urllib3.disable_warnings()

"""
Modify these please
"""
switchuser='admin'
switchpassword='Admin12345' 
mgmtip='10.10.20.101'

#client_cert_file='PATH_TO_CLIENT_CERTIFICATE'
#client_key_file='PATH_TO_CLIENT_KEY_FILE'
#ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='https://' + mgmtip + '/ins'
myheaders={'content-type':'application/json'}
payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "copy run start",
    "output_format": "json"
  }
})
#response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert_file_path,client_key_file),verify=ca_cert).json()
response = requests.post(url,data=payload, headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()
print(response)

