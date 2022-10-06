import time 
import board
import touchio
import digitalio as dio

touch_pad = board.A1
touch = touchio.TouchIn(touch_pad)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

while True:
    led.value = touch.value
    time.sleep(0.05)
