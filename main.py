import os
import random
from gpiozero import Device, Button
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer


button = Button(17, pull_up=True)  # Pin 10 on Raspberry Pi
sounds_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds')
sounds = [file for file in os.listdir(sounds_dir) if file.endswith('.wav') or file.endswith('.mp3')]

if not sounds:
    print("No sound files found in the 'sounds' folder.")
    exit()

mixer.init()

def play_random_sound():
    """Function to play a random sound from the 'sounds' folder."""
    sound_path = os.path.join(sounds_dir, random.choice(sounds))
    sound = mixer.Sound(sound_path)
    sound.play()

try:
    while True:
        button.wait_for_press()
        print("Button pressed!")
        play_random_sound()      # Play a random sound
        sleep(1)                 # Wait before allowing another playback

except KeyboardInterrupt:
    print("Program terminated by user.")
