import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [5, 6, 13, 19]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)





def  hacerTrago (alcohol, bebida, nivel):
    if(nivel==1): #inge
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(7)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(7)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(3)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(3)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==2): #medio
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(4)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(4)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(6)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(6)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==3): #suave
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(2)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(2)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(8)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(8)
             GPIO.output(19, GPIO.HIGH)

    return


#if __name__
"""
print('Empieza')
hacerTrago(2,2,1)
print('Listo')
"""
