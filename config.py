import requests as req
import json
req.packages.urllib3.disable_warnings()

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json"
}

url = "https://10.10.20.161/api/v0/authenticate"
data = json.dumps({
    'username': 'developer',
    'password': 'C1sco12345'
})
resp_token = req.post(url, headers=headers, data=data, verify=False)


HOST = "https://10.10.20.161"
BASE_URL = "{}/api/v0".format(HOST)
token = resp_token.json()

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {}".format(token)
}
