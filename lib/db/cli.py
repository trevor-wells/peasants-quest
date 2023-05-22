import os, sys, time, player, item, ascii_screens, movement, character
from colorama import Fore
from helpers import speak, clear_speak

cursor = "={=======- "
my_player = None

########## Game ##########
def game_options():
    ascii_screens.display_game_options()
    
def setup_game():
    clear_speak('Greetings! What is your name?\n', 0.03)
    all_player_names = [player.name for player in player.get_all_players()]
    valid_response = False
    while not valid_response:
        response = input(cursor)
        if response in all_player_names:
            clear_speak('I\'m sorry, but that name is already taken. Try a different one.\n', 0.02)
        else:
            global my_player
            my_player = player.find_player_by_name(response)
            valid_response = True
    clear_speak(f'Good luck on your adventure, {my_player.name}!')
    time.sleep(3)
    introduction()

def introduction():
    clear_speak(f'{Fore.RED}*BANG*\n\n', 0.03)
    time.sleep(0.5)
    speak('     *BANG*\n\n', 0.03)
    time.sleep(0.5)
    speak('          *BANG*\n\n', 0.03)
    time.sleep(1)
    speak(f'{Fore.GREEN}               Uggggghhh...\n\n')
    time.sleep(0.5)
    print(f'{Fore.RESET}You wake to the sound of loud knocking at your door.\n\n')
    time.sleep(1)
    speak(f'{Fore.CYAN}Hear ye, hear ye! Be it known to all citizens that our beloved King is dead! As there is no heir to the throne, the royal court is now accepting applications for the esteemed position of King!\n\n\n', 0.04)
    time.sleep(1.5)
    speak("""The only three requirements to apply are as follows...
    
        1. Slay a foul beast and present its severed head to the court.
        
        2. Acquire a fair maiden to take as your beloved queen.
        
        3. Do NOT smell like feces.\n\n""", 0.04)
    time.sleep(0.5)
    print(Fore.RESET + 'The crier slips a piece of paper under your door.\n\n')
    time.sleep(0.5)
    speak(f'{Fore.CYAN}Fare thee well, you stinky peasant!!\n\n{Fore.RESET}')
    game_loop()

def game_loop():
    while my_player.location_id != 10:
        prompt()
    win()

def prompt():
    print("What would you like to do?\n")
    response = input(cursor).lower().split()
    match response[0]:
        case 'help':
            print('Your command options are:\n\nmove - look - take - talk - inv - quit')
        case 'die' | 'unalive':
            die(my_player)
        case 'move' | 'walk' | 'travel' | 'go' | 'progress' | 'advance':
            if len(response) > 1:
                movement.player_move(my_player, response[1])
            else:
                movement.player_move(my_player)
        case 'look' | 'examine' | 'view':
            look()
        case 'grab' | 'take' | 'get' | 'pick up':
            if len(response) > 1:
                take(response[1])
            else:
                take()
        case 'talk' | 'speak':
            if len(response) > 1:
                talk(response[1])
            else:
                talk()
        case 'inv' | 'bag' | 'inventory' | 'items':
            inventory()
        case 'quit' | 'exit' | 'stop playing':
            confirm_quit()
        case _:
            print('I\'m not sure what you mean by that...')

def confirm_quit():
    os.system('clear')
    print('Are you sure you want to quit? Your progress will be saved.\n')
    valid_response = False
    while not valid_response:
        match input(cursor).lower():
            case 'yes' | 'yeah' | 'ya' | 'yup' | 'y':
                print('\nSee you next time, brave adventurer!\n')
                sys.exit()
            case 'no' | 'nvm' | 'nope' | 'nah' | 'n':
                print('\nOkay, resuming the game.\n')
                valid_response = True
            
def die(my_player):
    player.delete_player(my_player)
    print("That wasn\'t very smart of you. You dead.")
    sys.exit()
    
def look():
    item_descriptions = [item.description for item in my_player.location.items]
    character_descriptions = [character.description for character in my_player.location.characters]
    for description in character_descriptions:
        print('\n\n' + description)
    for description in item_descriptions:
        print('\n\n' + description)
    print('\n')

def take(desired_item = None):
    valid_response = False
    print('\nWhat do you want to take?\n')
    valid_items = [item.name for item in my_player.location.items]
    while not valid_response:
        if isinstance(desired_item, str):
            response = desired_item
            desired_item = None
        else:
            response = input(cursor).lower()
        match response:
            case desired_item if desired_item in valid_items:
                my_item = item.find_item_by_name(response)
                item.take_item(my_player, my_item)
                print(f'\nYou take the {response}.\n')
                valid_response = True
            case _:
                print(f'\nThere is no {response} in this area.\n')

def talk(desired_character = None):
    valid_response = False
    print('\n Who do you want to talk to?\n')
    valid_characters = [character.name for character in my_player.location.characters]
    while not valid_response:
        if isinstance(desired_character, str):
            response = desired_character
            desired_character = None
        else:
            response = input(cursor).lower()
        match response:
            case desired_character if desired_character in valid_characters:
                my_character = character.find_character_by_name(response)
                if response == 'dragon':
                    speak(f'\n{Fore.RED}' + my_character.phrase1 + f'\n\n{Fore.RESET}')
                else:
                    speak(f'\n{Fore.CYAN}' + my_character.phrase1 + f'\n\n{Fore.RESET}')
                valid_response = True
            case _:
                print(f'\nThere is no {response} in this area.\n')

def inventory():
    os.system('clear')
    print('Your Inventory:\n')
    for item in my_player.items:
        print(item.name + '\n')
    print('Feel free to look at any of your items, or type \'exit\' to exit your inventory.')
    response = input(cursor).lower().split()
    match response[0]:
        case 'look':
            if len(response) > 1:
                look_item(response[1])
            else:
                look_item()
        case 'exit':
            prompt()
        case _:
            inventory()

def look_item(desired_item = None):
    print("Which item would you like to inspect?")
    valid_response = False
    valid_items = [item.name for item in my_player.items]
    while not valid_response:
        if isinstance(desired_item, str):
            response = desired_item
            desired_item = None
        else:
            response = input(cursor).lower()
        if response in valid_items:
            match response:
                case 'map':
                    ascii_screens.display_map()
                case'application':
                    ascii_screens.display_application()
                case 'coin':
                    ascii_screens.display_coin()
                case 'oar':
                    ascii_screens.display_oar()
                case 'sword':
                    ascii_screens.display_sword()
                case 'axe':
                    ascii_screens.display_axe()
                case 'scarecrow':
                    ascii_screens.display_scarecrow()
                case 'octopus':
                    ascii_screens.display_octopus()
                case 'fair maiden':
                    ascii_screens.display_fair_maiden()
                case 'fishing rod':
                    ascii_screens.display_fishing_rod()
                case 'beer':
                    ascii_screens.display_beer()
            valid_response = True
        else:
            print("You don't even have that item... ")
        
def win():
    clear_speak(f'{Fore.GREEN}YOU WIN!')
    player.delete_player(my_player)
    sys.exit()
    
def generic_decision_tree():
    print("Question?")
    valid_response = False
    while not valid_response:
        response = input(cursor).lower().split()
        match response[0]:
            case 'something':
                if len(response) > 1:
                    pass
                    #somefunction(response[1])
                else:
                    pass
                    #somefunction()
                valid_response = True
            case 'another thing':
                pass
            case 'exit':
                pass
                #go back to previous page
                valid_response = true

if __name__ == '__main__':
    ascii_screens.display_title_screen()