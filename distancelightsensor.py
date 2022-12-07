import time
import board
import neopixel
import adafruit_hcsr04

np = neopixel.NeoPixel(board.A7, 30, brightness=0.5, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A5, echo_pin=board.A6)

black = [0, 0, 0]
red = [255, 0, 0]

def light_sensor(delay=0.01):
    np.fill(black)
    dis = 30 - (sonar.distance/5)
    for i in range(int(dis)):
        np[i] = red
    np.show()
    time.sleep(delay)

while True:
    try:
        light_sensor()
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

