import sys
import utils
import time

if sys.version_info[0] != 3:
    print("This script requires Python 3")

print("Enter name of the file you want create?")
name = input()
name = name + ".xml"

f = open(name, "w+")
firstphoto=""

def ask(i, count):
    global firstphoto
    utils.clear()
    print("Image %d/%d\n\n" %(i+1, count))
    while True:
        xtime = input("What's the time of the image apeearing? (from 00:00 to 23:59, e.g. 22:30)\n")
        try:
            hours = xtime[0:2]
            minutes = xtime[3:5]
            hours = int(hours)
            minutes = int(minutes)
            if(hours >=0 and hours <24):
                if(minutes >= 0 and minutes < 60):
                    if(xtime[2:3]== ":"):
                        break
                    else:
                        #fail on purpose because something doesn't meet the requirements
                        minutes=int("jp2gmd")
                else:
                    #fail on purpose because something doesn't meet the requirements
                    minutes=int("jp2gmd")
            else:
                #fail on purpose because something doesn't meet the requirements
                minutes=int("jp2gmd")
        except ValueError:
            print("Invalid time format! Try again!")
            time.sleep(2)
    seconds = (hours*3600) + minutes*60
    uri = input("Paste an absolute location of your photo (you can drag it onto this window)\n")
    if(i == 0):
        firstphoto = uri
    else:
        f.write("       <to>%s</to>\n"%(uri))
        f.write("   </transition>\n")
    f.write("   <!-- %s -->\n"%(xtime))
    f.write("   <static>\n")
    f.write("       <duration>%d.0</duration>\n"%(seconds))
    f.write("       <file>%s</file>\n"%(uri))
    f.write("   </static>\n")
    f.write('   <transition type="overlay">\n')
    f.write("       <duration>5.0</duration>\n")
    f.write("       <from>%s</from>\n"%(uri))
    if(count-1==i):
        f.write("       <to>%s</to>\n"%(firstphoto))
        f.write("   </transition>\n")
        f.write("</backgroud>")
    return

#beginning(open of <backgroud> and whole <starttime>)
f.write("<backgroud>\n   <starttime>\n       <year>2019</year>\n       <month>01</month>\n       <day>01</day>\n        <hour>00</hour>\n        <minute>00</minute>\n       <second>00</second>\n   </starttime>\n")
f.close()
while(1):
    count = input("How many pictures do you have?\n")
    try:
        count = int(count)
        break
    except ValueError:
        print("This value is not valid! Try again!")
        time.sleep(2)


for i in range(count):
    f = open(name, "a")
    ask(i, count)
    f.close()