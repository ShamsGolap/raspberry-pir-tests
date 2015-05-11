import RPi.GPIO as GPIO
import time
import os


pir = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(pir)
    if current_state != previous_state:
        new_state = 'HIGH' if current_state else 'LOW'

        if new_state == 'HIGH':
            os.system('mpg123 bonjour.mp3 &')

        else:
            os.system('mpg123 au_revoir.mp3 &')
