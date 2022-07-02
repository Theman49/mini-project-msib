from config import *
from utilities import *
from Labs import getIdLab
import json

def createInterfaces():
    id_labs = getIdLab('create interface on node in')
    print("id lab: {}".format(id_labs))
    node = input("node: ")
    slot = input("slot: ")

    endpoint = "/labs/{}/nodes/{}/wipe_disks".format(id_labs, node)
    URL = url(endpoint)
    req.put(URL, headers=headers, verify=False)

    endpoint = "/labs/{}/interfaces".format(id_labs)
    URL = url(endpoint)

    data = json.dumps({
        'node': node,
        'slot': int(slot)
    })


    print("Creating interface on node {} in lab with id {}...".format(node,id_labs))
    resp = req.post(URL, headers=headers, data=data, verify=False)
    print(resp.text)