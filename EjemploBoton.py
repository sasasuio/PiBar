from gpiozero import Button
from time import sleep

button_up = Button(16)
button_sel = Button(20)
button_down = Button(21)

#Tiempo de debounce
delay = 0.2

def check_up_button(delay):
    if(button_up.value == 1):
        print('UP')
        sleep(delay)
    return


while True:
    check_up_button(delay)

    if(button_sel.value == 1):
        print('SEL')
        sleep(delay)

    if(button_down.value == 1):
        print('DOWN')
        sleep(delay)


