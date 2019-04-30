#Test

import time
from sense_hat import SenseHat

sense = SenseHat()


r = 225
g = 0
b = 0

msleep = lambda x: time.sleep(x / 1000.0)

def next_colour():
    global r
    global g
    global b

    if (r == 225 and g < 225 and b == 0):
        g += 1

    if (g == 225 and r > 0 and b == 0):
        r -= 1

    if (g == 225 and b < 225 and r == 0):
        b += 1

    if (b == 225 and g > 0 and r == 0):
        g -= 1

    if (b == 225 and r < 225 and g == 0):
        r += 1

    if (r == 225 and g < 225 and b == 0):
        g += 1
    
    if (r == 225 and b > 0 and g == 0):
        b -= 1

while True:
    sense.clear([r, g, b])
    msleep(2)
    next_colour()