from config import *
from utilities import *
import json
import yaml
import time

# LABS
def createLab(getTitle: str):
    title = getTitle

    endpoint = "/labs?title={}".format(title)
    URL = url(endpoint)
    print("Creating Lab with title '{}' ...".format(title))
    resp = req.post(URL, headers=headers, verify=False)
    idlab = resp.json()
    return idlab['id']


#  NODES
def createNode(getId, data):
    id_labs = getId
    print("id lab: {}".format(id_labs))
    endpoint = "/labs/{}/nodes".format(id_labs)
    URL = url(endpoint)

    payload = json.dumps({
    "x": data['x'],
    "y": data['y'],
    "label": data['label'],
    "configuration": data['configuration'],
    "node_definition": data['node_definition'],
    "image_definition": data['image_definition'],
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
    resp = req.post(URL, headers=headers, data=payload, verify=False)
    return resp.text

def updateConfigNodes(getId, getNode, fileConfig):
    id_labs = getId
    print("id lab: {}".format(id_labs))
    node = getNode 
    config = fileConfig 

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
    return resp.text

# INTERFACES
def createInterfaces(getId, data):
    id_labs = getId
    print("id lab: {}".format(id_labs))

    endpoint = "/labs/{}/nodes/{}/wipe_disks".format(id_labs, data['node'])
    URL = url(endpoint)
    req.put(URL, headers=headers, verify=False)

    endpoint = "/labs/{}/interfaces".format(id_labs)
    URL = url(endpoint)

    payload = json.dumps({
        'node': data['node'],
        'slot': data['slot']
    })


    print("Creating interface on node {} in lab with id {}...".format(data['node'],id_labs))
    resp = req.post(URL, headers=headers, data=payload, verify=False)
    return resp.text


# LINKS
def createLinks(getId, data):
    id_labs = getId
    print("id lab: {}".format(id_labs))
    endpoint = "/labs/{}/links".format(id_labs)
    URL = url(endpoint)

    payload = json.dumps({
        'src_int': data['src_int'],
        'dst_int': data['dst_int']
    })

    print("Creating links in lab with id {}...".format(id_labs))
    resp = req.post(URL, headers=headers, data=payload, verify=False)
    return resp.text