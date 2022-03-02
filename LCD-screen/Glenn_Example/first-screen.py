#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    #logging.info("epd1in54b V2 Demo")

    epd = epd1in54b_V2.EPD()
    #logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)


    blackimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame


    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    drawblack = ImageDraw.Draw(blackimage)

    drawblack.rectangle((0, 10, 200, 34), fill = 255)
    drawblack.text((8, 12), 'Hello Denzel &', font = font, fill = 0)
    drawblack.text((8, 32), 'Hello Huxley!', font = font, fill = 0)



    drawblack.arc((90, 60, 150, 120), 0, 90, fill = 0)
    drawblack.rectangle((16, 130, 56, 180), fill = 0)
    drawblack.chord((90, 130, 150, 190), 0, 360, fill = 0)

    epd.display(epd.getbuffer(blackimage),epd.getbuffer(blackimage))



    drawblack.text((8, 60), 'I love you!!', font = font, fill = 0)
    epd.display(epd.getbuffer(blackimage),epd.getbuffer(blackimage))

    time.sleep(10)

    # read bmp file


    # read bmp file on window


    logging.info("Clear...")
    #epd.Clear()


    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd1in54b_V2.epdconfig.module_exit()
    exit()