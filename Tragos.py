import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinList = [5, 6, 13, 19]

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

def hacerTrago(alcohol,jugo,granadina,nivel)
	#Alcohol: 1 - Tequila / 2 - Vodka
	#Jugo: 0 - Nada / 1 - Naranja
	#Granadina: 0 - Nada / 1 - Granadina
	#Nivel: 1 - Suave / 2 - Medio / 3 - Ingeniería
	
	t_gran = 6
	t_ing_alc = 3
	t_ing_jug = 6
	t_med_alc = 2
	t_med_jug = 7
	t_low_alc = 2
	t_low_jug = 7
	t_shot = 2
	
	if(alcohol == 1) # Tequila
	
	
	
