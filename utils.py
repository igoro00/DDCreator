import os
from sys import platform
import time
from xml.etree import ElementTree
from xml.dom import minidom


def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # linux or os x and clear command needs to be used
        os.system('clear')
    elif platform == "win32":
        # windows and its clear command is weirdly cls instead of clear
        os.system('cls')
    return


def fail(r):
    # fail on purpose because something doesn't meet the requirements
    if (r == "ValueError"):
        minutes = int("jp2gmd")
    if (r == "NameError"):
        print(jp2gmd)


def askYN(q):
    yes = {'yes', 'y', 'ye', 'yass'}
    no = {'no', 'n', 'nope'}

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


def strToSec(strTime):
    hours = int(strTime[0:2])
    minutes = int(strTime[3:5])
    return (hours * 3600) + (minutes * 60)


def isTimeValid(timeInput):
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    hrsDigits = {'0', '1', '2'}
    minDigits = {'0', '1', '2', '3', '4', '5'}

    # hours at 1st char
    if (len(timeInput) >= 1) and (not hrsDigits.issuperset(timeInput[0])):
        return False
    # hours at 2nd char
    if (len(timeInput) >= 2) and (not digits.issuperset(timeInput[1])):
        return False
    #: at 3rd char
    if (len(timeInput) >= 3) and (timeInput[2] != ":"):
        return False
    # minutes at 4th char
    if (len(timeInput) >= 4) and (not minDigits.issuperset(timeInput[3])):
        return False
    # minutes at 5th
    if (len(timeInput) >= 5) and (not digits.issuperset(timeInput[4])):
        return False

    return True

def pathToFileName(path):
    output=""
    while path[-1] != '/':
        output = path[-1] + output
        path = path[:-1]
    return output

def compare_pArrays(pArray, pArray_bak):
    if len(pArray) != len(pArray_bak):
        return True

    for i in range(len(pArray)):
        if pArray[i].picture.strTime != pArray_bak[i].picture.strTime:
            return True
        if pArray[i].picture.path != pArray_bak[i].picture.path:
            return True
        if pArray[i].picture.transition != pArray_bak[i].picture.transition:
            return True

    return False

