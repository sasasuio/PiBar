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

def pantalla_bienvenida():
   draw.text((12,12),'Bienvenido',font=font)
   draw.text((24,22),'PiBar',font=font)
   return

def pantalla_sel_alcohol(item):
    c = '>'
    a = [0]*4
    a[item]=1
    title_1 = 'Seleccione: '
    item_1 = 'Shot Tequila'
    item_2 = 'Teq. Sunrise'
    item_3 = 'Vod. Sunrise'
    item_4 = 'Vodka Naran.'
    draw.text((4,-1), title_1, font=font)
    draw.text((4,15), a[0]*c+item_1,font = font)
    draw.text((4,23), a[1]*c+item_2,font = font)
    draw.text((4,31), a[2]*c+item_3,font = font)
    draw.text((4,39), a[3]*c+item_4,font = font)
    return

def pantalla_sel_nivel(lvl):
   c = '>'
   a = [0]*4
   a[lvl]=1
   title_1 = 'Nivel: '
   lvl_1 = 'Suave'
   lvl_2 = 'Medio'
   lvl_3 = 'Ingeniería'
   lvl_4 = 'Volver'
   draw.text((4,-1), title_1, font=font)
   draw.text((4,15), a[0]*c+lvl_1,font = font)
   draw.text((4,23), a[1]*c+lvl_2,font = font)
   draw.text((4,31), a[2]*c+lvl_3,font = font)
   draw.text((4,39), a[3]*c+lvl_4,font = font)
   return

def pantalla_preparando():
   draw.text((5,8),'Preparando...' ,font = font)
   #~ draw.rectangle((5,30,78,40), outline=0, fill=255)
   #~ imprimir_en_pantalla()
   #~ i=5
   #~ while i<78:
      #~ draw.rectangle((5,30,i,40), outline=0, fill=0)
      #~ i += 1
      #~ imprimir_en_pantalla()
      #~ sleep(0.05)
   #~ return

def pantalla_listo():
   draw.text((12,12),'Listo!',font=font)
   draw.text((24,22),'Disfruta',font=font)
   return



#Nivel Vertical: -1,15,23,31,39 (Delta 8)
#Pos X Máx = 83
#Pos Y Máx = 47

limpiar_pantalla()
pantalla_bienvenida()
imprimir_en_pantalla()
sleep(1)

for i in range(4):
    limpiar_pantalla()
    pantalla_sel_alcohol(i)
    imprimir_en_pantalla()
    sleep(0.5)

for i in range(4):
   limpiar_pantalla()
   pantalla_sel_nivel(i)
   imprimir_en_pantalla()
   sleep(0.5)

limpiar_pantalla()
pantalla_preparando()
imprimir_en_pantalla()
sleep(1)

limpiar_pantalla()
pantalla_listo()
imprimir_en_pantalla()
