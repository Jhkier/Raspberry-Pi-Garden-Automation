#!/usr/bin/python3

import time
import board
import busio
import digitalio
from board import *

from datetime import date

jet_Nozzle = digitalio.DigitalInOut(D5)
jet_Nozzle.direction = digitalio.Direction.OUTPUT

def spray_function():
    while True:
        jet_Nozzle.value = True
        time.sleep(6)               # how long its on for... make this 5 in future.
        jet_Nozzle.value = False
        time.sleep(10)              #how long off for - make this 300 for 5 minutes off

spray_function()