
# Copy of my code
#!/usr/bin/env python
"""
	Detects motion and outputs a sound via a piezo buzzer. 
"""


# Import GPO and time packages we will need in oour script
import RPi.GPIO as GPIO
import time

__author__ = "gus-pimylifeup"
__version__ = "1.0"
__maintainer__ = "pimylifeup.com"

# Created two variables to store our pin numbers in
pir_sensor = 11
piezo = 7

# setmode allows us to set the numbering we use for our pins
GPIO.setmode(GPIO.BOARD)

# Set piezo buzzer to be an output
GPIO.setup(piezo,GPIO.OUT)

# Ser pir sensor to be an input
GPIO.setup(pir_sensor, GPIO.IN)

# set current_state to be zero for boolean of false = 0, true = 1
current_state = 0

# Nested main functionality of code with in try except finaly block
try:
# Infinite while loop, can cancel script with contol c in terminal
    while True:
	# Put script to sleep for .1 seconds
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(piezo,True)
            time.sleep(1)
            GPIO.output(piezo,False)
            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
# Ensure script cleans up nicely
    GPIO.cleanup()

# Test Save 2
