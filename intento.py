import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)





def  hacerTrago (alcohol, bebida, nivel):
    if(nivel==1): #inge
        if(alcohol==1):#pisco
             GPIO.output(5,  GPIO.LOW)
             time.sleep(7)
             GPIO.output(5, GPIO.HIGH
        elif(alcohol==2)#ron
             GPIO.output(6, GPIO.LOW)
             time.sleep(7)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1)#blanca
             GPIO.output(13, GPIO.LOW)
             time.sleep(3)
             GPIO.output(13, GPIO.HIGH)
        elif(bebida==2)#negra
             GPIO.output(19, GPIO.LOW)
             time.sleep(3)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==2): #medio
             GPIO.output(5,  GPIO.LOW)
             time.sleep(4)
             GPIO.output(5, GPIO.HIGH
        elif(alcohol==2)#ron
             GPIO.output(6, GPIO.LOW)
             time.sleep(4)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1)#blanca
             GPIO.output(13, GPIO.LOW)
             time.sleep(6)
             GPIO.output(13, GPIO.HIGH)
        elif(bebida==2)#negra
             GPIO.output(19, GPIO.LOW)
             time.sleep(6)
             GPIO.output(19, GPIO.HIGH)

    if(nivel==3): #suave
                 GPIO.output(5,  GPIO.LOW)
             time.sleep(2)
             GPIO.output(5, GPIO.HIGH
        elif(alcohol==2)#ron
             GPIO.output(6, GPIO.LOW)
             time.sleep(2)
             GPIO.output(6, GPIO.HIGH)
        if(bebida==1)#blanca
             GPIO.output(13, GPIO.LOW)
             time.sleep(8)
             GPIO.output(13, GPIO.HIGH)
        elif(bebida==2)#negra
             GPIO.output(19, GPIO.LOW)
             time.sleep(8)
             GPIO.output(19, GPIO.HIGH)

    return




print('Empieza')
hacerTrago(1,2,2)
print('Listo')
