import board
import time
import random
import neopixel

np = neopixel.NeoPixel(board.A3, 30, brightness=0.5, auto_write=False)


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
purple = [255, 255, 0]
yellow = [0, 255, 255]
white = [255, 255, 255]
black = [0, 0, 0]
christmas_colors = (red, green, blue, purple, yellow)

def enter_santa(delay=0.5):
    i = 0
    for i in range(0, 3):
        np[i] = red
        if i == 1:
            np[i-1] = white
        if i >= 2:
            np[i-1] = white
            np[i-2] = red
    np.show()
    time.sleep(delay)

def santa(col_list, delay=0.5):
    i = 0
    for i in range(np.n):
        if i <= (np.n - 4):
            if i%2 == 0:
                np[i] = random.choice(col_list)
            else:
                np[i] = black
            np[i+1] = red
            np[i+2] = white
            np[i+3] = red
            np.show()
            time.sleep(delay)
            i+=4

enter_santa()
santa(christmas_colors)
