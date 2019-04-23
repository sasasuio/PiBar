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
        
def mostrar_menu(item,page):
	limpiar_pantalla()
	
	if(page == 1):
		draw.text((8,-1), 'Seleccione: ', font=font)
		if(item == 1):
			draw.text((8,15), '> Pisco',font = font)
			draw.text((8,23), 'Ron',font = font)
		if(item == 2):
			draw.text((8,15), 'Pisco',font = font)
			draw.text((8,23), '> Ron',font = font)
	
	if(page == 2):
		draw.text((8,-1), '¿Bebida? ', font=font)
		if(item==1):
			draw.text((8,15), '> Blanca',font = font)
			draw.text((8,23), 'Negra',font = font)
			draw.text((8,31), 'Volver',font = font)
		if(item==2):
			draw.text((8,15), 'Blanca',font = font)
			draw.text((8,23), '> Negra',font = font)
			draw.text((8,31), 'Volver',font = font)
		if(item==3):
			draw.text((8,15), 'Blanca',font = font)
			draw.text((8,23), 'Negra',font = font)
			draw.text((8,31), '> Volver',font = font)
	
	if(page ==3):
		draw.text((8,-1),'Nivel:',font=font)
		if(item==1):
			draw.text((8,15), '> Ingeniería',font = font)
			draw.text((8,23), 'Medio',font = font)
			draw.text((8,31), 'Bajo',font = font)
			draw.text((8,39), 'Volver', font = font)
		if(item==2):
			draw.text((8,15), 'Ingeniería',font = font)
			draw.text((8,23), '> Medio',font = font)
			draw.text((8,31), 'Bajo',font = font)
			draw.text((8,39), 'Volver', font = font)
		if(item==3):
			draw.text((8,15), 'Ingeniería',font = font)
			draw.text((8,23), 'Medio',font = font)
			draw.text((8,31), '> Bajo',font = font)
			draw.text((8,39), 'Volver', font = font)
		if(item==4):
			draw.text((8,15), 'Ingeniería',font = font)
			draw.text((8,23), 'Medio',font = font)
			draw.text((8,31), 'Bajo',font = font)
			draw.text((8,39), '> Volver', font = font)							
			
	imprimir_en_pantalla()
	return

#INICIALIZACIÓN Y VARIABLES DE MENÚ

page = 1
item = 1
page_prev = 1
item_prev = 1
items_page1 = 2
items_page2 = 3
items_page3 = 4

alcohol = 0
bebida = 0
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
		if(page == 3 and item == 0):
			item = items_page3
	
	if(down == 1):
		down = 0
		item += 1
		if(page == 1 and item == (items_page1+1)):
			item = 1
		if(page == 2 and item == (items_page2+1)):
			item = 1
		if(page == 3 and item == (items_page3+1)):
			item = 1
	
	if(sel == 1):
		sel = 0
		if(page == 1 and item == 1): #Selección Pisco
			page = 2
			item = 1
			alcohol = 1
			print('Selección: Pisco')
		elif(page == 1 and item == 2): #Selección Ron
			page = 2
			item = 1
			alcohol = 2
			print('Selección: Ron')
		elif(page == 2 and item == 1): #Selección Blanca
			page = 3
			item = 1
			bebida = 1
			print('Selección: Blanca')
		elif(page == 2 and item == 2): #Selección Negra
			page = 3
			item = 1
			bebida = 2
			print('Selección: Negra')
		elif(page == 2 and item == 3): #Selección Volver
			page = 1
			item = 1
			print('Volviendo a Menú Principal')
		elif(page == 3 and item == 1): #Nivel Ingeniero
			page = 1
			item = 2
			nivel = 1
			hacerTrago(alcohol,bebida,nivel)
			print('Nivel Ingeniería Seleccionado')
		elif(page == 3 and item == 2): #Nivel Medio
			page = 1
			item = 2
			nivel = 2
			hacerTrago(alcohol,bebida,nivel)
			print('Nivel Medio Seleccionado')
		elif(page == 3 and item == 3): #Nivel Bajo
			page = 1
			item = 2
			nivel = 3
			hacerTrago(alcohol,bebida,nivel)
			print('Nivel Bajo Seleccionado')
		elif(page == 3 and item == 4): #Selección Volver 
			page = 1
			item = 1
