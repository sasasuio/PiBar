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

    #GPIO 5: Tequila (Ex Pisco)
    #GPIO 6: Vodka (Ex Ron)
    #GPIO 13: Jugo (Ex Blanca)
    #GPIO 19: Granadina (Ex Negra)

	t_gran = 6
	t_ing_alc = 3
	t_ing_jug = 6
	t_med_alc = 2
	t_med_jug = 7
	t_low_alc = 2
	t_low_jug = 7
	t_shot = 2

    time_alc = [3,2,1]
    time_jug = [9,7,6]

	if(alcohol == 1) # Tequila
        if(jugo == 0) # Shot Tequila
            GPIO.output(5,GPIO.LOW)
            sleep(t_shot)
            GPIO.output(5,GPIO.HIGH)
        if(jugo == 1 and granadina == 1) # Tequila Sunrise
            #Surtir Tequila
            GPIO.output(5,GPIO.LOW)
            sleep(time_alc[nivel-1])
            GPIO.output(5,GPIO.HIGH)
            #Surtir Jugo
            GPIO.output(13,GPIO.LOW)
            sleep(time_jug[nivel-1])
            GPIO.output(13,GPIO.HIGH)
            #Surtir granadina
            GPIO.output(19,GPIO.LOW)
            sleep(t_gran)
            GPIO.output(19,GPIO.HIGH)
    if(alcohol == 2) #Vodka
        #Surtir Vodka
        GPIO.output(6,GPIO.LOW)
        sleep(t_shot)
        GPIO.output(6,GPIO.HIGH)
        #Surtir jugo
        GPIO.output(13,GPIO.LOW)
        sleep(t_shot)
        GPIO.output(13,GPIO.HIGH)
        if(granadina == 1)
            GPIO.output(19,GPIO.LOW)
            sleep(t_shot)
            GPIO.output(19,GPIO.HIGH)

    return
