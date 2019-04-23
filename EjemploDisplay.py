#Importar Librerías

from time import sleep

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont   

 
# Raspberry Pi hardware SPI config
# Conexión SPI por defecto:

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

#Creación de objeto display

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Inicializar librería
disp.begin(contrast=65)

# Limpiar el Display
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
     
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
     
# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
font = ImageFont.load_default()
     
# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
     
# Write some text.
draw.text((8,30), 'Hello World!', font=font)
     
# Display image.
disp.image(image)
disp.display()

def limpiar_pantalla():
        disp.clear()
        disp.display()
        draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        return

def imprimir_en_pantalla():
        disp.image(image)
        disp.display()

a = ['ab','abc','abcd','56','5','6','7','8']

while True:
        
    for i in range(len(a)):
        limpiar_pantalla()
        draw.rectangle((0,0,83,8), outline=0, fill=255)
        draw.rectangle((0,10,83,18), outline=0, fill=255)
        draw.rectangle((0,18,83,26), outline=0, fill=255)
        draw.rectangle((0,26,83,34), outline=0, fill=255)
        draw.rectangle((0,34,83,42), outline=0, fill=255)
        draw.rectangle((0,42,83,50), outline=0, fill=255)
        draw.text((8,-1), 'Hola Mundo', font=font)
        draw.text((8,17), a[i], font=font)
        imprimir_en_pantalla()
        print(a[i])
        sleep(0.5)

        
