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
        a.printHeader(i, True, picArray[-1].strTime)
        path = a.askPath()
        sumSecTime = sum(pic.secTime for pic in picArray)
        #print(sumSecTime)
    else:
        a.printHeader(i, False, "")
        path = a.askPath()
        sumSecTime = 0
        
    print()
    strTime = a.askTime(sumSecTime)
    picObject = pic(strTime, path, sumSecTime)
    picArray.append(picObject)

name = a.askXMLPath
if utils.askYN("Do you want to save your config to %s?(Y/n) "%(name)):
    print()
    write.write(picArray, name)
