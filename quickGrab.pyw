"""
 
All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized without the Bookmarks Toolbar enabled.
Down key has been hit 0 times the play area was already centered in
the browser.
x_pad = 304
y_pad = 219
Play area =  x_pad+1, y_pad+1, 796, 825
"""



import ImageGrab
import os
import time


# Globals
# ------------------
 
x_pad = 304
y_pad = 219
 
def screenGrab():
    box = (x_pad+1, y_pad+1,x_pad+640,y_pad+479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()


def get_seat_one():
    box = (25,62,25+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 #130, 56    130,78
def get_seat_two():
    box = (126,62,126+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 #230,58     230,76   
def get_seat_three():
    box = (227,63,227+63,63+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 #322,60     329,76
def get_seat_four():
    box = (328,64,328+63,64+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 #431,58
def get_seat_five():
    box = (429,63,429+63,63+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (530,63,530+63,63+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()
