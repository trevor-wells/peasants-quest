import os, shutil, sys, time

########## Typed Text ##########
def speak(phrase, speed = 0.05):
    os.system('clear')
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


########### Center Text ##########
def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))

