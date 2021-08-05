#!/usr/bin/python3

import time
import board
import busio
import digitalio
from board import *

from datetime import date

jet_Nozzle = digitalio.DigitalInOut(D5)    #should change the pin
jet_Nozzle.direction = digitalio.Direction.OUTPUT

jet_Spray_led = digitalio.DigitalInOut(D6)  #should change the pin too
jet_Spray_led.direction = digitalio.Direction.OUTPUT

def spray_function():
    while True:
        jet_Nozzle.value = True
        jet_Spray_led = True
        time.sleep(6)               # how long its on for... make this 5 in future.
        jet_Nozzle.value = False
        jet_Spray_led = False
        time.sleep(10)              #how long off for - make this 300 for 5 minutes off

spray_function()