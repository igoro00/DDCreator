class pic:
    def __init__(self, strTime, path, sumSecTime):
        self.strTime = strTime
        self.secTime = self.strToSec(strTime, sumSecTime)
        self.path = path
        
    def strToSec(self, strTime, sumSecTime):
        hours = int(strTime[0:2])
        minutes = int(strTime[3:5])
        return (hours*3600) + (minutes*60) - sumSecTime

