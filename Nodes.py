from config import *
from utilities import *
from Labs import getIdLab
import json

def createNode():
    id_labs = getIdLab('create node in')
    print("id lab: {}".format(id_labs))
    endpoint = "/labs/{}/nodes".format(id_labs)
    URL = url(endpoint)
    x = input("x: ")
    y = input("y: ")
    label = input('label: ')
    configuration = input('configuration: ')
    node_definition = input("node_definition: ")
    image_definition = input("image_definition: ")

    data = json.dumps({
    "x": int(x),
    "y": int(y),
    "label": label,
    "configuration": configuration,
    "node_definition": node_definition,
    "image_definition": image_definition,
    "ram": None,
    "cpus": None,
    "cpu_limit": None,
    "data_volume": None,
    "boot_disk_size": None,
    "tags": [
        ""
    ]
    })

    print("Creating node in lab with id {}...".format(id_labs))
    resp = req.post(URL, headers=headers, data=data, verify=False)
    print(resp.text)

def updateConfigNodes():
    id_labs = getIdLab('update configuration node in')
    print("id lab: {}".format(id_labs))
    node = input("node: ")
    config = input("config path file: ")

    f = open(config, 'r')
    payload = f.read()
    f.close()


    endpoint = "/labs/{}/nodes/{}/wipe_disks".format(id_labs, node)
    URL = url(endpoint)
    req.put(URL, headers=headers, verify=False)

    endpoint = "/labs/{}/nodes/{}/config".format(id_labs, node)
    URL = url(endpoint)

    headers['Content-Type'] = "text/plain"
    resp = req.put(URL, headers=headers, data=payload, verify=False)
    print(resp.text)

def deleteNode():
    id_labs = getIdLab('delete node in')
    print("id lab: {}".format(id_labs))
    node = input("node: ")

    endpoint = "/labs/{}/nodes/{}/wipe_disks".format(id_labs, node)
    URL = url(endpoint)
    req.put(URL, headers=headers, verify=False)

    endpoint = "/labs/{}/nodes/{}".format(id_labs, node)
    URL = url(endpoint)

    resp = req.delete(URL, headers=headers, verify=False)
    print(resp.text)
