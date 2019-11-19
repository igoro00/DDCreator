import utils
import time

def ask(f, i, count):
    utils.clear()
    print("Image %d/%d\n\n" %(i+1, count))
    while True:
        time = input("What's the time of the image apeearing? (from 00:00 to 23:59, e.g. 22:30)\n")
        try:
            hours = time[0:2]
            minutes = time[3:5]
            hours = int(hours)
            minutes = int(minutes)
            if((hours >=0 and hours <24) or (minutes >=0 and minutes < 60) and time[2:3] == ":"):
                break
            else:
                #fail on purpose
                minutes=int("jp2gmd")
        except ValueError:
            print("Invalid time format! Try again!")
            time.sleep(5)
    return