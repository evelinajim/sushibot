"""
 
All coordinates assume a screen resolution of 1920x1080, and Chrome 
maximized without the Bookmarks Toolbar enabled.
Down key has been hit 0 times the play area was already centered in
the browser.
x_pad = 304
y_pad = 219
Play area =  x_pad+1, y_pad+1, 796, 825

to stop execution, click in the shell and hit Ctrl+C to send a keyboard interrupt.
"""



import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *   #now we don't have to call numpy.array() just array()
                      # * imports everything


# Globals
# ------------------
 
x_pad = 304
y_pad = 219

 #this part get us the screenshot of the game and the box
def screenGrab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+479)
    im = ImageGrab.grab(box)
 
    ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab():
    box = (x_pad+1,y_pad+1,x_pad+640,y_pad+479)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

 
def main():
    startGame()
    while True:
        check_bubs()
        

#Mouse left-click
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")          #completely optional. But nice for debugging purposes.


#Holding the mouse key down for longer. For shooting, dragging, etc.
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

#MAYBE READD THE GET CORDS SET CURSER BUTTON IDK
    #special ways to coords
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
     x,y = win32api.GetCursorPos()
     x = x - x_pad
     y = y - y_pad
     print(x,y)
     

def startGame():
    #location of first menu
    mousePos((343, 197))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((321, 382))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((588, 449))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((314, 372))
    leftClick()
    time.sleep(.1)

#coordinates of food
class Cord:
     
    f_shrimp = (39,331)
    f_rice = (95, 332)
    f_nori = (35, 380)
    f_roe = (95, 381)
    f_salmon = (34, 433)
    f_unagi = (88, 439)


#-----------------------------------    
     
    phone = (580, 354)
 
    menu_toppings = (516, 272)
     
    t_shrimp = (490, 217)
    t_nori = (488, 270)
    t_roe = (573, 268)
    t_salmon = (492, 261)
    t_unagi = (573, 208)
    t_exit = (594, 328)
 
    menu_rice = (534, 291)
    buy_rice = (544, 280)
     
    delivery_norm = (489, 288)






    
def clear_tables():
    mousePos((98, 204))
    leftClick()
 
    mousePos((197, 205))
    leftClick()
 
    mousePos((285, 206))
    leftClick()
 
    mousePos((386, 204))
    leftClick()
 
    mousePos((485, 207))
    leftClick()
 
    mousePos((598, 204))
    leftClick()
    time.sleep(1)


"""
 
Plate cords:
 
    98, 204
    197, 205
    294, 204
    406, 206
    502, 206
    598, 204
"""

def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

#dictionary of food items available at the beginning
#GLOBALS MORE


foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

sushiTypes = {3954:'onigiri', 
              4211:'caliroll',
              3881:'gunkan',}

class Blank:
    seat_1 = 7714
    seat_2 = 5986
    seat_3 = 13253
    seat_4 = 10280
    seat_5 = 5831
    seat_6 = 7384

def makeFood(food):
    if food == 'caliroll':
        print('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print('Making a onigiri')
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print('Making a gunkan')
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)


'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
'''

#CHECK FOR FOOD REPLENISHMENT 
def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print('%s is low and needs to be replenished' % i)
                buyFood(i)
        else:
            if j<4:
                print('need to buy %s' % i)
                print('only have %d on hand' % j)
                buyFood(i)


def buyFood(food):
     
    mousePos(Cord.phone)
     
    mousePos(Cord.menu_toppings)
     
     
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
     
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)
     
    mousePos(Cord.delivery_norm)


#replinish food and see if we have enough funds to do so.
    #opening menu item to buy food or nah

def buyFood(food):
     
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (109, 123, 127):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10     
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
 
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (15, 14, 4):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10         
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (127, 61, 0):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10                
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)



#WOW. coords. 30,55    29,80    25.62

def get_seat_one():
    box = (x_pad+25,y_pad+62,x_pad+25+63,y_pad+62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a

 #130, 56    130,78
def get_seat_two():
    box = (x_pad+126,y_pad+62,x_pad+126+63,y_pad+62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a

 #230,58     230,76   
def get_seat_three():
    box = (x_pad+225,y_pad+62,x_pad+225+63,y_pad+62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a

 #322,60     329,76
def get_seat_four():
    box = (x_pad+326,y_pad+62,x_pad+326+63,y_pad+62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a

 #431,58
def get_seat_five():
    box = (x_pad+427,y_pad+62,x_pad+427+63,y_pad+62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_six():
    box = (x_pad+528,y_pad+62,x_pad+528+63,y_pad+62+16)
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


#GIVING CONTROL TO THE BOT

def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
            makeFood(sushiTypes[s1])
        else:
            print('sushi not found!\n sushiType = %i' % s1)
 
    else:
        print('Table 1 unoccupied')
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
            makeFood(sushiTypes[s2])
        else:
            print('sushi not found!\n sushiType = %i' % s2)
 
    else:
        print('Table 2 unoccupied')
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
            makeFood(sushiTypes[s3])
        else:
            print('sushi not found!\n sushiType = %i' % s3)
 
    else:
        print('Table 3 unoccupied')
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
            makeFood(sushiTypes[s4])
        else:
            print('sushi not found!\n sushiType = %i' % s4)
 
    else:
        print('Table 4 unoccupied')
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
            makeFood(sushiTypes[s5])
        else:
            print('sushi not found!\n sushiType = %i' % s5)
 
    else:
        print('Table 5 unoccupied')
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s6])
            makeFood(sushiTypes[s6])
        else:
            print('sushi not found!\n sushiType = %i' % s6)
 
    else:
        print('Table 6 unoccupied')
 
    clear_tables()
