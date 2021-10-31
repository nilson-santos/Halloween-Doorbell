import os
import random
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled high (on)

sounds = next(os.walk(os.path.dirname(os.path.realpath(__file__))+'/sounds'), (None, None, []))[2]
mixer.init()

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        sound = mixer.Sound(f"sounds/{random.choice(sounds)}")
        sound.play()
        sleep(4)
