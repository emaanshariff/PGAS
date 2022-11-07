#imports from library necessary for function
import neopixel
import board
import time
import random
import digitalio as dio
import touchio


#define neopixel
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

#defining button, touch pads, and led
button_a = dio.DigitalInOut(board.BUTTON_A)
button_a.direction = dio.Direction.INPUT
button_a.pull = dio.Pull.DOWN
touch1 = touchio.TouchIn(board.A5)
touch2 = touchio.TouchIn(board.A6)
touch3 = touchio.TouchIn(board.A1)
touch4 = touchio.TouchIn(board.A2)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

#stores randomized numeric values for randomization of displaying colors
color_list = []

#stores user input in numeric values
user_color = 0
#keeps track of index in color_list in
count = 0

#variable to test if the game should start
game_start = False
#variable to test if button_a was pressed
button_start = False

#creating variables for different colors displayed in the game
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]
black = [0, 0, 0]


"""
Function name: add_color_list
Description:adds a random number to color_list to represent a color
Parameters: list - a list to append random numbers to (mainly used for color_list)
Return value: none
"""
def add_color_list(list):
    list.append(random.randint(1, 4))


"""
Function name: correct
Description: flashes a green light for when the user gets a sequence right
Parameters: delay - time delayed between neopixel lights (floating point)
Return value: none
"""
def correct(delay=0.1):
    for i in range(2):
        np.fill(green)
        np.show()
        time.sleep(delay)
        np.fill(black)
        np.show()
        time.sleep(delay)


"""
Function name: wrong
Description: flashes a red light for when the user gets a sequence wrong
Parameters: delay - time delayed between neopixel lights (floating point)
Return value: none
"""
def wrong(delay=0.1):
    for i in range(2):
        np.fill(red)
        np.show()
        time.sleep(delay)
        np.fill(black)
        np.show()
        time.sleep(delay)


"""
Function name: display_color
Description: checks value from add_color_list() and relates it to a color and displays the color
Parameters: list - a list to append random numbers to (mainly used for color_list); delay - time delayed between neopixel lights (floating point)
Return value: none
"""
def display_color(list, delay=0.2):
    for item in list:
        if item == 1:
            np[0] = red
            np[1] = red
            np.show()
            time.sleep(delay)
            np[0] = black
            np[1] = black
            np.show()
            time.sleep(delay)
        else:
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
        if item == 2:
            np[3] = green
            np[4] = green
            np.show()
            time.sleep(delay)
            np[3] = black
            np[4] = black
            np.show()
            time.sleep(delay)
        else:
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
        if item == 3:
            np[5] = blue
            np[6] = blue
            np.show()
            time.sleep(delay)
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
        else:
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)
        if item == 4:
            np[8] = yellow
            np[9] = yellow
            np.show()
            time.sleep(delay)
            np[8] = black
            np[9] = black
            np.show()
            time.sleep(delay)
        else:
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(delay)


"""
Function name: compare_lists
Description: compares the user input to the color_list to check if the user remembered the right color; is used primarily in user_input 
Parameters: user - user input from user_input; color - color_list
Return value: True or False
"""
def compare_lists(user, color):
    global count
    if user == color[count]:
        if count == len(color) - 1:
            correct()
        return True
    else:
        return False

"""
Function name: reset
Description: resets variables and lists to default when the game is over
Parameters: none
Return value: none
"""    
def reset():
    global color_list, game_start
    color_list = []
    game_start = False

"""
Function name: user_input
Description: tests sensor user input and assigns a number associated with a certain color that will be tested against color_list using the compare_lists() function
and uses either the wrong() or correct() function to display if the user got the sequence right
Parameters: delay - time delayed between neopixel lights (floating point)
Return value: none
"""   
def user_input(delay=0.1):
    global count
    for index in range(len(color_list)):
        while not touch1.value and not touch2.value and not touch3.value and not touch4.value:
            pass
        if touch1.value == True:
            np[0] = red
            np[1] = red
            np.show()
            time.sleep(delay)
            user_color = 1
        else:
            np[0] = black
            np[1] = black
            np.show()
            time.sleep(0.01)
        if touch2.value == True:
            np[3] = green
            np[4] = green
            np.show()
            time.sleep(delay)
            user_color = 2
        else:
            np[3] = black
            np[4] = black
            np.show()
            time.sleep(0.01)
        if touch3.value == True:
            np[5] = blue
            np[6] = blue
            np.show()
            time.sleep(delay)
            user_color = 3
        else:
            np[5] = black
            np[6] = black
            np.show()
            time.sleep(0.01)
        if touch4.value == True:
            np[8] = yellow
            np[9] = yellow
            np.show()
            time.sleep(delay)
            user_color = 4
        else:
            np[8] = black
            np[9] = black
            np.show()
            time.sleep(0.01)
        count = index
        value = compare_lists(user_color, color_list)
        if value == False:
            wrong()
            reset()

#tests if user presses start button. If button_a is true, it starts game by putting previous functions in order
while True:
    if not game_start:
        if button_a.value:
            button_start = not button_start
            time.sleep(.5)
            game_start = True
    else:
        add_color_list(color_list)
        display_color(color_list)
        user_input()


