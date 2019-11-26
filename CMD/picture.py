class pic:
    #
    #this class only holds data for one picture at a time
    #its not supposed to do anything except storing data
    #
    def __init__(self, path, strTime, transition):
        self.strTime = strTime
        self.path = path
        self.transition = float(transition)

