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
    t_ing_h = 126
    t_ing_l = 54
    t_med_h = 72
    t_med_l = 108
    t_sua_h = 36
    t_sua_l = 144

    if(nivel==1): #ingeniero
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(t_ing_h)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(t_ing_h)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(t_ing_l)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(t_ing_l)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==2): #medio
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(t_med_h)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(t_med_h)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(t_med_l)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(t_med_l)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==3): #suave
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             sleep(t_sua_h)
             GPIO.output(5, GPIO.HIGH)
        if(alcohol==2):#ron
             GPIO.output(6, GPIO.LOW)
             sleep(t_sua_h)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1):#blanca
             GPIO.output(13, GPIO.LOW)
             sleep(t_sua_l)
             GPIO.output(13, GPIO.HIGH)
        if(bebida==2):#negra
             GPIO.output(19, GPIO.LOW)
             sleep(t_sua_l)
             GPIO.output(19, GPIO.HIGH)

    return


#if __name__
"""
print('Empieza')
hacerTrago(2,2,1)
print('Listo')
"""
