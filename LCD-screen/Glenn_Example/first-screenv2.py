#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd1in54_V2 Demo")

    epd = epd1in54_V2.EPD()
    epd.init(0)
    epd.Clear(0xFF)
    time.sleep(1)

    # Drawing on the image
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    cicledraw = ImageDraw.Draw(image)


    epd.displayPartBaseImage(epd.getbuffer(image))

    epd.init(1)



    YAxis = 1
    XAxis = 1
    counter = 1
    degreeStart = 0
    circlebackground = ImageDraw.Draw(image)
    while (True):
        circlebackground.rectangle((XAxis-10, YAxis, XAxis + 20, YAxis + 20), fill = 255)
        cicledraw.chord(((XAxis), (YAxis), (XAxis + 20), (YAxis + 20)), 0, 360, fill = 0)
        cicledraw.arc((80, 130, 140, 190), 0, (degreeStart), fill = 0)
        epd.displayPart(epd.getbuffer(image))
        XAxis = XAxis + 10
        degreeStart = degreeStart + 20
        counter = counter + 1
        if (counter == 20):
            break


    drawblack = ImageDraw.Draw(image)


    drawblack.text((8, 12), 'Hello Denzel &', font = font, fill = 0)
    epd.displayPart(epd.getbuffer(image))
    drawblack.text((8, 32), 'Hello Huxley!', font = font, fill = 0)
    epd.displayPart(epd.getbuffer(image))


     # into partial refresh mode
    time_draw = ImageDraw.Draw(image)
    num = 0
    while (True):
        time_draw.rectangle((10, 60, 120, 100), fill = 255)
        time_draw.text((10, 60), time.strftime('%H:%M:%S'), font = font, fill = 0)
        #newimage = image.crop([10, 10, 120, 50])
        #image.paste(newimage, (10,10))
        epd.displayPart(epd.getbuffer(image))
        num = num + 1
        if(num == 20):
            break



except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd1in54_V2.epdconfig.module_exit()
    exit()
