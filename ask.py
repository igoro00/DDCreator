import time
import utils
class ask:
    def __init__(self, count):
        self.count = count

    def isLater(self, sumSecTime, current):
        if sumSecTime > 0:
            return (current - sumSecTime)>0
        else:
            return True
    
    def printHeader(self, i, doLastStrTime, lastSrtTime):
        utils.clear()
        print("Image %d/%d\n" %(i+1, self.count))
        if(doLastStrTime):
            print("Last picture is set to show at %s\n"%(lastSrtTime))

    def askTime(self, sumSecTime):
        while True:
            strTime = input("What's the time you want to show that picture at? (from 00:00 to 23:59, e.g. 22:30)\n")
            try:
                hours = int(strTime[0:2])
                minutes = int(strTime[3:5])
                seconds = (hours*3600) + (minutes*60)
                if(0 <= hours <= 23 and 0 <= minutes <= 59 and strTime[2:3]==":"):
                    if(self.isLater(sumSecTime, seconds)):
                        break
                    else:
                        utils.fail("NameError")
                else:
                    #crash try() and force user to try again
                    utils.fail("ValueError")
            except ValueError:
                print("Invalid time format! Try again")
                time.sleep(2)
            except NameError:
                print("This image must be set later than the last one! Try again")
                time.sleep(2)
        print()
        return strTime

    def askPath(self):
        cPath = None
        while True:
            path = input("Paste an absolute path to your picture e.g. /home/igor/Pictures/1.jpg (you can drag it onto this windows, but NO 'QUOTES' OR SPACES ALLOWED)\n")
            
            if utils.pathIsBroken(path): cPath = utils.fixPath(path) 
            #call autocorrect if its somehow broken

            if cPath is not None:
                #if it had to be changed
                print("\n\nIt looks like your path has some illegal attributes\nlike 'quotes' or spaces before or after the proper path.")
                print("So we tried to change it.")
                print("%s => %s\n"%(path, cPath))
                if utils.askYN("Is it a valid path to your picture?(Y/n) ") is False:
                    print("\nWell... Then you have to type it again")
                    #and the loop loops around again
                else:
                    #you user agreed that this is a valid path
                    path = cPath
                    break
            else:
                #it didn't change
                break

        return path
