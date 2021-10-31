import os
import random
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled high (on)

sounds = next(os.walk(os.path.dirname(os.path.realpath(__file__))+'/sounds'), (None, None, []))[2] # Returns a list of files in the sounds folder
mixer.init() # Starts the mixer

while True: # Run forever
    if GPIO.input(10) == GPIO.LOW: # Read the GPIO pin
        sound = mixer.Sound(f"sounds/{random.choice(sounds)}") # Choose a random sound from the list of sounds
        sound.play() # Play the sound
        sleep(4) # Wait for 4 seconds and repet the loop
