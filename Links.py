from config import *
from utilities import *
from Labs import getIdLab
import json

def createLinks():
    id_labs = getIdLab('create link in')
    print("id lab: {}".format(id_labs))
    endpoint = "/labs/{}/links".format(id_labs)
    URL = url(endpoint)
    src_int = input("src_int: ")
    dst_int = input("dst_int: ")

    data = json.dumps({
        'src_int': src_int,
        'dst_int': dst_int
    })

    print("Creating links in lab with id {}...".format(id_labs))
    resp = req.post(URL, headers=headers, data=data, verify=False)
    print(resp.text)