import cmd
import textwrap
import sys
import os
import time
import random
from speak import speak
from lib.models import Player

cursor = "={=======- "
screen_width = 100
my_player = Player()

##### Title Screen #####
def title_screen_selections():
    option = input(cursor)
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input(cursor)
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('clear')
    print(' ###############################')
    print(' # Welcome to Peasant\'s Quest #')
    print(' ###############################')
    print('            - PLAY -            ')
    print('            - HELP -            ')
    print('            - QUIT -            ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print(' ################################')
    print(' #           Help Menu          #')
    print(' ################################')
    print(' - I don\'t know how to help you.')
    title_screen_selections()

def start_game():
    setup_game()


##### MAP #####
"""
     -----------------
  4  |   |   |   |   |
    -----------------
  3  |   |   |   |   |
     -----------------
  2  |   |   |   |   |
     -----------------
  1  |   |   |   |   |
     -----------------
       a   b   c   d
"""
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up, north'
DOWN = 'down, south'
LEFT = 'left, west'
RIGHT = 'right, east'

solved_places = {
    'a4': False, 'b4': False, 'c4': False, 'd4': False,
    'a3': False, 'b3': False, 'c3': False, 'd3': False,
    'a2': False, 'b2': False, 'c2': False, 'd2': False,
    'a1': False, 'b1': False, 'c1': False, 'd1': False
    }

zone_map = {
    'a1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'c1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'd1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'a2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'b2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'c2': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'd2': {
        ZONENAME: 'start',
        DESCRIPTION: 'You wake in a dark room.',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'a3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'b3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'c3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'd3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'a4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'b4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'c4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
    'd4': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'up, north',
        DOWN: 'down, south',
        LEFT: 'left, west',
        RIGHT: 'right, east'
    },
}


##### GAME INTERACTIVITY #####
def print_location():
    print('\n' + ('#' * (4 + len(my_player.location))))
    print('#' + my_player.location.upper() + ' #')
    print('# ' + zone_map[my_player.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(my_player.location))))

def prompt():
    print("\n" + "=======================")
    print("What would you like to do?")
    action = input(cursor)
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'look', 'interact', 'die']
    while action.lower() not in acceptable_actions:
        print("Bro I literally have no idea what you're saying.")
        action = input(cursor)
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() == 'die':
        print("You've made the right choice. There is no defeating John Truong the Mighty. You dead.")
        sys.exit()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_look(action.lower())

def player_move(action):
    ask = "Where would you like to move to?"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zone_map[my_player.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zone_map[my_player.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zone_map[my_player.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zone_map[my_player.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print('\n' + "You have moved to the " + destination + ".")
    my_player.location = destination
    print_location()

def player_look(action):
    if zone_map[my_player.location][SOLVED]:
        print("You have already exhausted this zone.")
    else:
        print("Trigger puzzle here.")

##### GAME FUNCTIONALITY #####
def main_game_loop():
    while my_player.game_over is False:
        prompt()
    #handle if puzzles have been solved, boss defeated, game won, etc.

def setup_game():
    os.system('clear')

    ### NAME COLLECTING ###
    question1 = "Hello, what's your name?\n"
    speak(question1)
    player_name = input(cursor)
    my_player.name = player_name

    ### CLASS ASSIGNMENT ###
    question2 = f'Alright, {my_player.name}. What is your role?\n\n Mage - Warrior - Rogue - Archer\n'
    valid_roles = ['mage', 'warrior', 'rogue', 'archer', 'priest']
    speak(question2)
    player_job = input(cursor)
    while player_job.lower() not in valid_roles:
        speak(f'Sorry, you cannot be a {player_job}. Please pick from the following options: \n\n Mage - Warrior - Rogue - Archer - Priest')
        player_job = input(cursor)
    my_player.job = player_job

    ### PLAYER STATS ###

    ### INTRODUCTION ###
    os.system('clear')
    intro = player_name + " the " + player_job + "... You have been tasked with a quest. You must save the world from "
    for character in intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    pause =  "..... "
    for character in pause:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    villain = "John Truong"
    for character in villain:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)
    os.system('clear')
    print('####################')
    print('#   Let us begin!  #')
    print('####################')
    time.sleep(0.5)
    main_game_loop()

    


title_screen()