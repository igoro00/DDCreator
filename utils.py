import os
from sys import platform
import time

def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin": 
        #linux or os x and clear command needs to be used
        os.system( 'clear' )
    elif platform == "win32":
        #windows and its clear command is weirdly cls instead of clear
        os.system( 'cls' )
    return

def fail():
    #fail on purpose because something doesn't meet the requirements
    minutes=int("jp2gmd")

def askYN(q):
    yes = {'yes','y', 'ye', 'yass'}
    no = {'no','n', 'nope'}

    while True:
        choice = input(q).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
          print("Please respond with 'yes' or 'no'")
          time.sleep(2)