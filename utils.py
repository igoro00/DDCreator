import os
from sys import platform
import time
from xml.etree import ElementTree
from xml.dom import minidom

def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin": 
        #linux or os x and clear command needs to be used
        os.system( 'clear' )
    elif platform == "win32":
        #windows and its clear command is weirdly cls instead of clear
        os.system( 'cls' )
    return

def fail(r):
    #fail on purpose because something doesn't meet the requirements
    if(r == "ValueError"):
        minutes=int("jp2gmd")
    if(r == "NameError"):
        print(jp2gmd)

def askYN(q):
    yes = {'yes','y', 'ye', 'yass'}
    no = {'no','n', 'nope'}

    while True:
        choice = input(q).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
          print("Please respond with 'yes' or 'no'")
          time.sleep(2)

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def pathIsBroken(path):
    if (path[0] is not "/") or (path[-1] in {" ", "'"}):
        return True
    return False

def fixPath(path):
    keepFixing = True
    while keepFixing:
        if path[0] is not "/":
            path = path[1:]
        if path[-1] in {" ", "'"}:
            path = path[:-1]
        keepFixing = pathIsBroken(path)
    return path
