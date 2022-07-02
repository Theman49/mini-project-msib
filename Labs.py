from utilities import *
import json
import yaml
import time

def showDetailLab(labs):
    clear()
    print("="*30)
    print("no |\t\tdetails")
    print("="*30)
    for i in range(len(labs)):
        print("{}. ".format(str(i+1)), end="")
        pp.pprint(labs[i])


def getLabs():
    # get all id of labs
    URL = url('/labs')
    resp = req.get(URL, headers=headers, verify=False)

    labs = []

    # get detail of each lab from id
    for id_lab in resp.json():
        #URL = "{}/labs/{}".format(BASE_URL, id_lab)
        endpoint = "/labs/" + id_lab
        URL = url(endpoint)
        lab = req.get(URL, headers=headers, verify=False)
        labs.append(lab.json())

    # show the detail lab in screen
    return labs

def getIdLab(process: str):
    labs = getLabs()
    check = False
    lab_no = 0
    while check == False:
        lab_no = input("{} lab no : ".format(process))
        if lab_no.isdigit():
            lab_no = int(lab_no)
            if lab_no > 0 and lab_no <= len(labs):
                check = True
            else:
                print("only input lab no that show in screen!")
        else:
            print("only input lab no that show in screen!")
        

    id_labs = labs[lab_no-1]['id']
    return id_labs


def startLab():
    id_labs = getIdLab('start')

    endpoint = "/labs/{}/start".format(id_labs)
    URL = url(endpoint)

    print("Starting Lab with id {} ...".format(id_labs))
    resp = req.put(URL, headers=headers, verify=False)
    print("status: "+ resp.json())

def stopLab():
    id_labs = getIdLab('stop')

    endpoint = "/labs/{}/stop".format(id_labs)
    URL = url(endpoint)

    print("Stoping Lab with id {} ...".format(id_labs))
    resp = req.put(URL, headers=headers, verify=False)
    print("status: "+ resp.json())

def createLab():
    title = input("lab title : ")

    endpoint = "/labs?title={}".format(title)
    URL = url(endpoint)
    print("Creating Lab with title '{}' ...".format(title))
    resp = req.post(URL, headers=headers, verify=False)
    print(resp.text)

def deleteLab():
    id_labs = getIdLab('delete')

    endpoint = "/labs/{}/wipe".format(id_labs)
    URLwipe = url(endpoint)


    print("Deleting Lab id {} ...".format(id_labs))

    endpoint = "/labs/{}".format(id_labs)
    URL = url(endpoint)
    ask = input("Realy want to delete lab {} ? (y/n): ".format(id_labs))
    if ask == 'y' or ask == "":
        req.put(URLwipe, headers=headers, verify=False)
        resp = req.delete(URL, headers=headers, verify=False)
        print(resp)
    else:
        print("cancelling...")
        time.sleep(1)
        return

def getTopologyLab():
    id_labs = getIdLab('get topology')

    endpoint = "/labs/{}/topology".format(id_labs)
    URL = url(endpoint)

    print("Processing get topology {}...".format(id_labs))

    headers['Accept'] = 'text/plain'
    resp = req.get(URL, headers=headers, verify=False)
    ask = input('do u want to save the topology to the file? (y/n): ')
    if ask == 'y' or ask == "":
        location = './topology/lab_{}.json'.format(id_labs)
        f = open(location, 'w')
        f.write(resp.text)
        f.close()

        with open(location, 'r') as jsonfile:
            jsonread = json.load(jsonfile)

        location2 = "./topology/lab_{}.yaml".format(id_labs)
        f = open(location2, 'w')  
        f.write(yaml.dump(jsonread))
        f.close()

        print("Success save topology in {} and {}".format(location, location2))
        time.sleep(2)
    elif ask == 'n':
        pp.pprint(resp.json())
