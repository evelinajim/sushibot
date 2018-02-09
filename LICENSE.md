# sushibot
This is my sushibot and all the problems along the way

import ImageGrab
import os
import time

//this takes a snapshot
def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
