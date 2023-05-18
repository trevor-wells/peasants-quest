import os, sys, time, player, location, item, shutil, ascii_screens, helpers, movement
cursor = "={=======- "
my_player = player.find_player_by_name('Greg')
########## Game ##########
def game_options():
    ascii_screens.display_game_options()
    
def setup_game():
    helpers.speak('Greetings! What is your name?\n', 0.01)
    player.give_player_name(my_player, input(cursor))
    helpers.speak(f'{my_player.name}, is it? Well, {my_player.name}... You have a grand adventure ahead of you! Let\'s not dilly dally. Good luck!', 0.01)
    time.sleep(2)
    introduction()

def introduction():
    os.system('clear')
    print('You wake in your house.\n\n')
    game_loop()

def game_loop():
    while my_player:
        prompt()

def prompt():
    print("What would you like to do?\n")
    response = input(cursor).lower().split()
    match response[0]:
        case 'help':
            print('Your command options are:\nmove - look - take = die')
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
            take()
        case 'inv' | 'bag' | 'inventory' | 'items':
            inventory()
        case _:
            print('I\'m not sure what you mean by that...')

def die(my_player):
    player.delete_player(my_player)
    print("That wasn\'t very smart of you. You dead.")
    sys.exit()
    
def look():
    print(my_player.location.look + '\n')

def take(desired_item = None):
    valid_items = [item.name for item in my_player.location.items]
    while desired_item == None:
        print('What do you want to take?')
        response = input(cursor).lower()
        match response:
            case desired_item if desired_item in valid_items:
                my_item = item.find_item_by_name(response)
                item.take_item(my_player, my_item)
                print(f'You take the {response}.')
            case _:
                print(f'There is no {response} in this area.')

def inventory():
    os.system('clear')
    print('Your Inventory:\n')
    for item in my_player.items:
        print(item.name + '\n')
    print('Feel free to look at any of your items, or type \'exit\' to exit your inventory.')
    match input(cursor):
        case 'look':
            look_item()
        case 'exit':
            prompt()
        case _:
            inventory()

def look_item():
    print("Which item would you like to inspect?")
    valid_items = [item.name for item in my_player.items]
    response = input(cursor).lower()
    match response:
        case desired_item if desired_item in valid_items:
            if response == 'map':
                ascii_screens.display_map()
            else:
                print(item.find_by_name(response).description)
        case _:
            print("You don't even have that item... ")
    
if __name__ == '__main__':
    ascii_screens.display_title_screen()