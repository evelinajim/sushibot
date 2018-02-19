# sushibot
This is my sushibot and all the problems along the way


## Requirements

* Python 3.6 32-bit
* Pycharm 3.6 32-bit
* Libraries needed: `The Python Imaging Library (Pillow)`, `Numpy`, and `pypiwin32`
* Paint program like paint.net
* 1920 x 1080 screen users

## Setup for 1920 x 1080 users

```sh
$ pip install -r requirements.txt
```

* Open the game (https://www.miniclip.com/games/sushi-go-round/en/) and fullscreen your screen. The corner must be to the right hand. You may need to adjust coordinates. 
* You can check if your mouse lines up with the game coordinates by running quickgrab.py

## Setup for other users
* Open the game (https://www.miniclip.com/games/sushi-go-round/en/) and fullscreen your screen.
* use quickgrab.py to take a picture of your full screen and then go on paint.net to get the coordinates of the game. Make sure your only capturing the game.

![table](https://cdn.tutsplus.com/active/uploads/legacy/tuts/425_pythonBot/Images/sushi_zoom_set_xy.png)

# Features
* starts the game/skips menu: startGame()
* refills ingredients
* makes sushi
* wins the first round
* clears tables

## Run game

def main():
    
    startGame()
     while True:
        check_bubs()


