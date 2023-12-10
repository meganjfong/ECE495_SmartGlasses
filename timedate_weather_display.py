#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_1in51
from PIL import Image, ImageDraw, ImageFont

import requests
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

city = 'Durham'

url = 'https://api.openweathermap.org/data/2.5/weather?q=Durham,US%22&units=imperial&APPID=1d1f5f8a0bf8111bb8cfe9d3774bef8f'

res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']

print('Temperature:', temp, 'C')
print('Wind:', wind)
print('Humidity: ', humidity)
print('Description:', description)

try:
    disp = OLED_1in51.OLED_1in51()

    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    # Create blank image for drawing.
    spaces = r"              "
    show = spaces + str(temp) + u'\N{DEGREE SIGN}' + 'F ' + '\n' + spaces + str(description) + '\n'
    current_datetime = datetime.now()
    formatted_date = spaces + current_datetime.strftime("%Y-%m-%d")
    formatted_time = spaces + current_datetime.strftime("%H:%M")
    
    image1 = Image.new('1', (disp.width, disp.height), 'WHITE')
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    logging.info("***draw text")
    draw.text((0, 0), show, font=font1, fill=0)
    draw.text((0, 30), formatted_date, font=font1, fill=0)
    draw.text((0, 50), formatted_time, font=font1, fill=0)
    
    image1 = image1.rotate(90)
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(10)
    
    disp.clear()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    OLED_1in51.config.module_exit()
    exit()
