#
# Import GPO and time packages we will need in oour script
#
import RPi.GPIO as GPIO
import time

#
# Created three variables to store our pin numbers in
#
pir_sensor = 11 # Pin GPIO17
piezo = 7	# Pin GPIO4
LED = 40	# Pin GPIO21

#
# setmode allows us to set the numbering we use for our pins
#
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)


#
# Set piezo buzzer to be an output
#
GPIO.setup(piezo,GPIO.OUT)

#
# Set pir sensor to be an input
#
GPIO.setup(pir_sensor, GPIO.IN)

#
# Set LED to be an output
#
GPIO.setup(LED, GPIO.OUT)

#
# set current_state to be zero for boolean of false = 0, true = 1
#
current_state = 0

#
# Nested main functionality of code with in try except finaly block
#
try:
# Infinite while loop, can cancel script with contol c in terminal
    while True:
	# Put script to sleep for .1 seconds
        time.sleep(0.1)
        # Check current state
        current_state = GPIO.input(pir_sensor)  # Sensor checks for motion
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(piezo,True)		# Buzzer on
            GPIO.output(40, GPIO.HIGH)  	# LED on
            time.sleep(.5)               	# Hold for .5 second
            GPIO.output(piezo,False)    	# Buzzer off
            GPIO.output(40, GPIO.LOW)   	# LED off
            time.sleep(5)               	# Wait for 5 seconds
except KeyboardInterrupt:
    pass
finally:
# Ensure script cleans up nicely
    GPIO.cleanup()

# Test Save 2
