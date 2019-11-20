import sys
import utils
import time
import ask
import write

if sys.version_info[0] != 3:
    print("This script requires Python 3")

while(1):
    count = input("How many pictures do you have?\n")
    try:
        count = int(count)
        break
    except ValueError:
        print("This value is not valid! Try again!")
        time.sleep(2)

a = ask.ask(count)

for i in range(count):
    a.askTime(i)
    a.askPhotos()

write.write(a.getTimeArray(), a.getTimeSecArray, a.getPhotosArray, count)
