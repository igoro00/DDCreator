import time
import utils
class ask:
    def __init__(self, count):
        self.count = count
        self.timeArray=[]
        self.photosArray=[]

    def getTimeArray(self):
        return self.timeArray

    def getPhotosArray(self):
        return self.photosArray


    def askTime(self, i):
        utils.clear()
        print("Image %d/%d\n\n" %(i+1, self.count))
        while True:
            tyTime = input("What's the time of the image apeearing? (from 00:00 to 23:59, e.g. 22:30)\n")
            try:
                hours = tyTime[0:2]
                minutes = tyTime[3:5]
                hours = int(hours)
                minutes = int(minutes)
                if(0 <= hours <= 23 and 0 <= minutes <= 59 and tyTime[2:3]==":" ):
                    #its correct time format and we dont need to fail
                    break
                else:
                    #crash try() and force user to try again
                    utils.fail()
            except ValueError:
                print("Invalid time format! Try again!")
                time.sleep(2)
        self.timeArray.append((hours*3600) + minutes*60)
    
    def askPhotos(self):
        self.photosArray.append(input("Paste an absolute location of your photo (you can drag it onto this window)\n"))