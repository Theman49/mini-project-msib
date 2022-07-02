from os import system, name
from config import *
import pprint
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

def clear():
    if name == "posix":
        system("clear")
    else:
        system("cls")

def url(endpoint: str):
    URL = BASE_URL + endpoint
    return URL