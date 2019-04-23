import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [5, 6, 13, 19]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  while True:
    GPIO.output(5, GPIO.LOW)
    print ("ONE")
    time.sleep(SleepTimeL); #!/usr/bin/python3
    GPIO.output(6, GPIO.LOW)
    print ("TWO")
    time.sleep(SleepTimeL);  
    GPIO.output(13, GPIO.LOW)
    print ("THREE")
    time.sleep(SleepTimeL);
    GPIO.output(19, GPIO.LOW)
    print ("FOUR")
    time.sleep(SleepTimeL);
    print ("Good bye!")
    for i in pinList: 
      GPIO.setup(i, GPIO.OUT) 
      GPIO.output(i, GPIO.HIGH)
    time.sleep(5);

  # End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
