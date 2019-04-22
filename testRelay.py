import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #Inicia y hace posible la configuracion

#pin 5
GPIO.setup(5,GPIO.OUT) #inicia la configuracion
GPIO.output(5,GPIO.HIGH) #se declara OFF

#pin 6
GPIO.setup(6,GPIO.OUT) #inicia la configuracion
GPIO.output(6,GPIO.HIGH) #se declara OFF

#pin 13
GPIO.setup(13,GPIO.OUT) #inicia la configuracion
GPIO.output(13,GPIO.HIGH) #se declara OFF

#pin 19
GPIO.setup(19,GPIO.OUT) #inicia la configuracion
GPIO.output(19,GPIO.HIGH) #se declara OFF

try:
	GPIO.output(5,GPIO.LOW) #se delcara ON
	print("Primer relay ON")
	time.sleep(2)
	
	GPIO.output(6,GPIO.LOW) #se delcara ON
	print("Segundo relay ON")
	time.sleep(2)

	GPIO.output(13,GPIO.LOW) #se delcara ON
	print("Tercer relay ON")
	time.sleep(2)
	
	GPIO.output(19,GPIO.LOW) #se delcara ON
	print("Cuarto relay ON")
	time.sleep(2)

GPIO.cleanup()
	print("Todos apagados")

except KeyboradInterrupt:
	print("Salir")
	GPIO.cleanup()import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #Inicia y hace posible la configuracion

#pin 5
GPIO.setup(5,GPIO.OUT) #inicia la configuracion
GPIO.output(5,GPIO.HIGH) #se declara OFF

#pin 6
GPIO.setup(6,GPIO.OUT) #inicia la configuracion
GPIO.output(6,GPIO.HIGH) #se declara OFF

#pin 13
GPIO.setup(13,GPIO.OUT) #inicia la configuracion
GPIO.output(13,GPIO.HIGH) #se declara OFF

#pin 19
GPIO.setup(19,GPIO.OUT) #inicia la configuracion
GPIO.output(19,GPIO.HIGH) #se declara OFF

try:
	GPIO.output(5,GPIO.LOW) #se delcara ON
	print("Primer relay ON")
	time.sleep(2)
	
	GPIO.output(6,GPIO.LOW) #se delcara ON
	print("Segundo relay ON")
	time.sleep(2)

	GPIO.output(13,GPIO.LOW) #se delcara ON
	print("Tercer relay ON")
	time.sleep(2)
	
	GPIO.output(19,GPIO.LOW) #se delcara ON
	print("Cuarto relay ON")
	time.sleep(2)

GPIO.cleanup()
	print("Todos apagados")

except KeyboradInterrupt:
	print("Salir")
	GPIO.cleanup()