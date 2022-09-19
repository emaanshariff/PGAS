import board
import time
import random
import neopixel

np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

def sparkle(background, foreground, loop = 10, delay=0.1):
  for outer in range(loop):
    np.fill(background)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = foreground
    np.show()
    time.sleep(delay)

def chase(background, foreground, loop=10, delay=0.1):
  result = 0
  for outer in range(loop):
    np.fill(background)
    for i in range(np.n):
      if i % 3 == result:
        np[i] = foreground
    np.show()
    time.sleep(delay)
    result = (result + 1) % 3
