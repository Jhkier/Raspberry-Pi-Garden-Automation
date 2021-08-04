#!/usr/bin/python3

import time
import board
import busio
import digitalio
from board import *

from datetime import date

water_level_led = digitalio.DigitalInOut(D5)
water_level_led.direction = digitalio.Direction.OUTPUT

water_level_sensor = digitalio.DigitalInOut(D18)
water_level_sensor.switch_to_input(pull=digitalio.Pull.UP)
water_level_sensor.pull = digitalio.Pull.UP

def water_level_function():
    current_water_level = None
    while True:
        water_high = water_level_sensor.value
        if water_high != current_water_level:
            water_changed(water_high)
        current_water_level = water_high
        time.sleep(60)

def water_changed(water_high: bool):
        water_level_led.value = water_high
        if water_high == True:
            print("They System has Water")
        else:
            print("The System is Dry and needs Water")



water_level_function()