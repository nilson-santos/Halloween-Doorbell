import os
import random
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

sounds = next(os.walk(os.path.dirname(os.path.realpath(__file__))+'/sounds'), (None, None, []))[2]
mixer.init()

sound = mixer.Sound(f"sounds/{random.choice(sounds)}")
sound.play()
sleep(4)
