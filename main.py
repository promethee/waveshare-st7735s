#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import digitalio
import board
import LCD_1in44
import LCD_Config
from PIL import Image, ImageDraw, ImageFont, ImageColor
from fonts.ttf import RobotoMedium


ROTATION = int(os.environ.get('ROTATION', 0))
WIDTH = os.environ.get('WIDTH', 128)
HEIGHT = os.environ.get('HEIGHT', 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (255, 0, 255),
    (255, 0, 128),
]

index = 0

font_smiley = ImageFont.truetype('./CODE2000.TTF', 24)
font = ImageFont.truetype(RobotoMedium, 24)
img = Image.new("RGB", (WIDTH, HEIGHT), 0)
draw = ImageDraw.Draw(img)

LCD = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
LCD.LCD_Init(Lcd_ScanDir)

def show_credits():
    global index
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=BLACK)
    draw.text((int(WIDTH*0.09), int(HEIGHT*0.1)), "¯\_(ツ)_/¯", font=font_smiley, fill=COLORS[index])
    draw.text((int(WIDTH*0.09), int(HEIGHT*0.4)), "promethee", font=font, fill=COLORS[index])
    draw.text((int(WIDTH*0.2), int(HEIGHT*0.7)), "@github", font=font, fill=COLORS[index])
    rotated_img = img.rotate(ROTATION)
    LCD.LCD_ShowImage(rotated_img,0,0)
    LCD_Config.Driver_Delay_ms(500)

while True:
    index = index + 1 if index < len(COLORS) - 1 else 0
    show_credits()
