import os
import sys
import time

def speak(phrase, speed = 0.05):
    os.system('clear')
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)