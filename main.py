import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.items = []
        self.location = 'start'

myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('clear')
    print(' _______________________________')
    print('|  Welcome to Peasant\'s Quest  |')
    print(' _______________________________')
    print('            - PLAY -            ')
    print('            - HELP -            ')
    print('            - QUIT -            ')
    title_screen_selections()

def help_menu():
    print(' _______________________________')
    print('|  Welcome to Peasant\'s Quest  |')
    print(' _______________________________')
    print('  HELP MENU ')
    title_screen_selections()

def start_game():
    print('START MENU')
    title_screen_selections()


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

zonemap = {
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
    'd2': {
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
