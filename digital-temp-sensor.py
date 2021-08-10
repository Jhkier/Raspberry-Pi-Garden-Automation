#import modules

import time
import board
import busio
import digitalio
from board import *

from datetime import date


#DigitalIO and Pin setup
tempLed = digitalio.DigitalInOut(D17)                  #PIN LED for too hot sensor.
tempLed.direction = digitalio.Direction.OUTPUT

tempSensor = digitalio.DigitalInOut(D14)              #Temp sensor DS18B20 as configured in terminal
tempSensor.switch_to_input(pull=digitalio.Pull.UP)
tempSensor.pull = digitalio.Pull.UP


#main loop
try:
    while 1:
        tempStore = open("/sys/bus/w1/devices/28-3cffe076cfcf/w1_slave")	#change this number to the Device ID of your sensor
        data = tempStore.read()
        tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = temperature/1000
        print(temperature)

        if temperature > 24:	#change this value to adjust the 'too hot' threshold
            tempLed.value = True
        else:
            tempLed.value = False

        time.sleep(1)


except KeyboardInterrupt:
    digitalio.cleanup()
    print ("Program Exited Cleanly")