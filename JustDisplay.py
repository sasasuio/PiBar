#Delays
from time import sleep
#Para Display:
	#Librerías Adafruit:
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
	#Librerías Imágenes:
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#INICIALIZACIÓN Y VARIABLES DEL DISPLAY

#Puerto SPI
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

#Objeto Display e Inicializar
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=65)
#Limpiar Display
disp.clear()
disp.display()

#Crear imagen en blanco para dibujar de 1 bit
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

#Creación de objeto para dibujar
draw = ImageDraw.Draw(image)
#Dibuja un rectángulo blanco para limpiar el display
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

#Carga Fuente (Tipografía)
font = ImageFont.load_default()

def limpiar_pantalla():
	disp.clear()
	disp.display()
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
	return

def imprimir_en_pantalla():
    disp.image(image)
    disp.display()
    return

#Nivel Vertical: -1,15,23,31,39

limpiar_pantalla()
draw.text((4,-1), 'Seleccione: ', font=font)
draw.text((4,15), 'Shot Tequila',font = font)
draw.text((4,23), '>Tequila Sunrise',font = font)
draw.text((4,31), 'Vodka Sunrise',font = font)
draw.text((4,39), 'Vodka Naranja',font = font)
imprimir_en_pantalla()
sleep(2)
limpiar_pantalla()
draw.text((4,-1), 'Seleccione Nivel:',font = font)
draw.text((4,15), 'Suave',font = font)
draw.text((4,23), 'Medio',font = font)
draw.text((4,31), 'Ingeniería',font = font)
imprimir_en_pantalla()
