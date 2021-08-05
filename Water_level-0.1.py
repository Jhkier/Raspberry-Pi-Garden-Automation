#!/usr/bin/python3

import time
import board
import busio
import digitalio
from board import *

from datetime import date

water_level_led = digitalio.DigitalInOut(D5)                  #PIN TO PUMP
water_level_led.direction = digitalio.Direction.OUTPUT

water_level_sensor = digitalio.DigitalInOut(D18)              #PIN to WATER LEVEL SENSOR
water_level_sensor.switch_to_input(pull=digitalio.Pull.UP)
water_level_sensor.pull = digitalio.Pull.UP

def water_level_function():
    current_water_level = None
    while True:
        water_low = water_level_sensor.value
        if water_low != current_water_level:
            water_changed(water_low)
        current_water_level = water_low
        time.sleep(6)                                # INCREASE TO 60 TO CHECK EVERY MIN

def water_changed(water_low: bool):
        water_level_led.value = water_low
        if water_low == True:
            print("The system is dry and needs water")
        else:
            print("The System has water")



water_level_function()