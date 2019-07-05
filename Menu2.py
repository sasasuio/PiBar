#IMPORTAR LIBRERÍAS

#Para Botones:
from gpiozero import Button
from time import sleep
#Para Display:
	#Librerías Adafruit:
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
	#Librerías Imágenes:
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from intento import hacerTrago

#INICIALIZACIÓN Y VARIABLES DE BOTONES

#Declaración Pins Botones
button_up = Button(16)
button_sel = Button(20)
button_down = Button(21)

#Tiempo de debounce entre botones
delay = 0.2

#Variables de Estado de Botones
up = 0
sel = 0
down = 0

#Funciones para chequear botones
def check_up_button(delay):
	if(button_up.value == 1):
		print('UP')
		sleep(delay)
		return 1
	else:
		return 0

def check_sel_button(delay):
	if(button_sel.value == 1):
		print('SEL')
		sleep(delay)
		return 1
	else:
		return 0

def check_down_button(delay):
	if(button_down.value == 1):
		print('DOWN')
		sleep(delay)
		return 1
	else:
		return 0

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
   return

def pantalla_listo():
   draw.text((12,12),'Listo!',font=font)
   draw.text((24,22),'Disfruta',font=font)
   return

def mostrar_menu(item,page):
	limpiar_pantalla()

	if(page == 0):
		pantalla_bienvenida()
	if(page == 1):
		pantalla_sel_alcohol(item-1)
	if(page == 2):
		pantalla_sel_nivel(item-1)
	if(page == 3):
		pantalla_preparando()
	if(page == 4):
		pantalla_listo()

	imprimir_en_pantalla()
	return

#INICIALIZACIÓN Y VARIABLES DE MENÚ

page = 0
item = 1
page_prev = 0
item_prev = 1
items_page1 = 4
items_page2 = 4

alcohol = 0
jugo = 0
granadina = 0
nivel = 0



#LOOP PRINCIPAL DEL PROGRAMA

mostrar_menu(item,page)

while True:

	#Si hay cambios en item o menu...
	if(page != page_prev or item != item_prev):
		page_prev = page
		item_prev = item
		#...Actualizar la pantalla
		mostrar_menu(item,page)

	up = check_up_button(delay)
	sel = check_sel_button(delay)
	down = check_down_button(delay)

	if(up == 1):
		up = 0
		item -= 1
		if(page == 1 and item == 0):
			item = items_page1
		if(page == 2 and item == 0):
			item = items_page2

	if(down == 1):
		down = 0
		item += 1
		if(page == 1 and item == (items_page1+1)):
			item = 1
		if(page == 2 and item == (items_page2+1)):
			item = 1

	if(sel == 1):
		sel = 0
		if(page == 1 and item == 1): #Selección Shot Tequila
			page = 3 #Prepara inmediatamente
			item = 1
			alcohol = 1
			jugo = 0
			granadina = 0
		elif(page == 1 and item == 2): #Selección Tequila Sunrise
			page = 2
			item = 1
			alcohol = 1
			jugo = 1
			granadina = 1
		elif(page == 1 and item == 2): #Selección Vodka Sunrise
			page = 2
			item = 1
			alcohol = 2
			jugo = 1
			granadina = 1
		elif(page == 1 and item == 1): #Selección Vodka Naranja
			page = 2
			item = 1
			alcohol = 2
			jugo = 1
			granadina = 0
		elif(page == 2 and item == 1): #Selección Suave
			page = 3
			item = 1
			nivel = 1
		elif(page == 2 and item == 2): #Selección Medio
			page = 3
			item = 1
			nivel = 2
		elif(page == 2 and item == 3): #Selección Ingeniería
			page = 3
			item = 1
			nivel = 3
		elif(page == 2 and item == 4): #Selección Volver
			page = 1
			item = 1
		elif(page == 3):
			hacerTrago(alcohol,jugo,granadina,nivel)
		elif(page == 4):
			sleep(2)
			page = 1
			item = 1
