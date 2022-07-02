import time
import json
from utilities import *

import Labs
import Nodes
import Interfaces
import Links




def main():
    intro = """
===============
Menu:
===============
0. exit
1. start lab
2. stop lab
3. create lab
4. delete lab
5. get topology lab

6. create node
7. delete node
8. update config node

9. create interfaces

10. create links
===============
"""
    print(intro, end="")
    cek = False
    while(cek == False):
        choose = input("choose (1-9) / 0 for exit: ")
        if choose == '0':
            cek = True
            print("Goodbye!!!")
            exit()
        if choose == '1':
            Labs.startLab()
            cek = True
        elif choose == '2':
            Labs.stopLab()
            cek = True
        elif choose == '3':
            Labs.createLab()
            cek = True
        elif choose == '4':
            Labs.deleteLab()
            cek = True
        elif choose == '5':
            Labs.getTopologyLab()
            cek = True
        elif choose == '6':
            Nodes.createNode()
            cek = True
        elif choose == '7':
            Nodes.deleteNode()
            cek = True
        elif choose == '8':
            Nodes.updateConfigNodes()
            cek = True
        elif choose == '9':
            Interfaces.createInterfaces()
            cek = True
        elif choose == '10':
            Links.createLinks()
            cek = True
        elif choose == 'refresh':
            return


    time.sleep(5)
    clear()
while True:
    print("Getting Labs...")
    labs = Labs.getLabs()
    Labs.showDetailLab(labs)
    main()