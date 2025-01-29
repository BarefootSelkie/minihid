#!/usr/bin/env python3

# from inky.auto import auto
from inky import InkyWHAT
from PIL import Image, ImageDraw, ImageFont, ImageOps
import datetime
import yaml
import logging
import requests
import json
import argparse
import time

# Arguments, Logging, Settings
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug level logging")
args = parser.parse_args()

if args.debug:
  # If arg -d or --debug passed in endale debug logging
  logging.basicConfig(format="%(asctime)s : %(message)s", filename="debug.log", encoding='utf-8', level=logging.DEBUG)
else:
  # Otherwise use warn logging
  logging.basicConfig(format="%(asctime)s : %(message)s", filename="warning.log", encoding='utf-8', level=logging.WARN)

### Constants ###
inky = InkyWHAT('red')
colour = {
  "black": inky.BLACK,
  "white": inky.WHITE,
  "red": inky.RED
}

# Fonts
fontGridSingle = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(44))
fontGridDual = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(24))
fontGridLabel = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(18))

fontSizeCalSm = 24
fontSizeCalBg = fontSizeCalSm * 2
fontCalBg = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(fontSizeCalBg))
fontCalSm = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(fontSizeCalSm))

# Sizing for calendar
frameCalendar = 4
anchorCalendar = (400-128,0)
paddingVCalendar = 2
widthCalendar = 128
heightCalendar = 128

# Draw the calendar square in top right of screen
def drawCalendar(image):
  dateNumber = datetime.date.today().strftime('%d')
  dateDay = datetime.date.today().strftime('%a')
  dateMonth = datetime.date.today().strftime('%b')

  print("Day number")
  print(dateNumber)
  print(dateDay)

  image.rounded_rectangle([anchorCalendar,(anchorCalendar[0] + widthCalendar, anchorCalendar[1] + heightCalendar)], radius=12, fill=None, outline=colour["red"], width=frameCalendar)
  image.rounded_rectangle([anchorCalendar,(anchorCalendar[0] + widthCalendar, anchorCalendar[1] + 32)], radius=12, fill=colour["red"], outline=colour["red"], width=frameCalendar, corners=(True, True, False, False))
  image.text(((anchorCalendar[0] + (widthCalendar // 2)), anchorCalendar[1] + frameCalendar + paddingVCalendar + (fontSizeCalSm // 2)), dateMonth, colour["white"], font=fontCalSm, anchor="mm")
  image.text(((anchorCalendar[0] + (widthCalendar // 2)), anchorCalendar[1] + (heightCalendar//2)), dateNumber, colour["black"], font=fontCalBg, anchor="mm")
  image.text(((anchorCalendar[0] + (widthCalendar // 2)), anchorCalendar[1] + heightCalendar - ((fontSizeCalSm // 2) + paddingVCalendar + frameCalendar)), dateDay, colour["black"], font=fontCalSm, anchor="mm")

display = Image.new(mode="P", size=(400,300), color=(inky.WHITE))
image = ImageDraw.Draw(display)
drawCalendar(image)
inky.set_image(display)
inky.show()

