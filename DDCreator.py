#!/usr/bin/python3
import sys
import utils
import time
from CMD import ask
import write
from CMD.picture import pic

if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit()

while(1):
    count = input("How many pictures do you have?\n")
    try:
        count = int(count)
        break
    except ValueError:
        print("This value is not valid! Try again!")
        time.sleep(2)

a = ask.ask(count)
picArray = []
for i in range(count):
    if len(picArray)>0:
        lastStrTime = picArray[-1].strTime
        a.printHeader(i, True, lastStrTime)
    else:
        lastStrTime = "00:00"
        a.printHeader(i, False, lastStrTime)

    path = a.askPath()
    print()
    strTime = a.askTime(lastStrTime)
    picObject = pic(path, strTime, 5)
    picArray.append(picObject)

name = a.askXMLPath()
if utils.askYN("Do you want to save your config to %s?(Y/n) "%(name)):
    print()
    write.write(picArray, name)
