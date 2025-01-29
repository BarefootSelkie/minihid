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


# Fonts
fontGridSingle = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(44))
fontGridDual = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(24))
fontGridLabel = ImageFont.truetype("./ttf/Fredoka-Medium.ttf", int(18))


inky = InkyWHAT('red')

display = Image.new(mode="P", size=(400,300), color=(inky.WHITE))
image = ImageDraw.Draw(display)
image.text((100, 100), "walandablap", inky.BLACK, font=fontGridSingle, anchor="ma")
inky.set_image(display)
inky.show()