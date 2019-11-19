import os
from sys import platform

def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin": 
        #linux or os x and clear command needs to be used
        os.system( 'clear' )
    elif platform == "win32":
        #windows and its clear command is weirdly cls instead of clear
        os.system( 'cls' )
    return