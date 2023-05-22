import os, player, location
cursor = "={=======- "

def player_move(my_player, destination = None):
    valid_response = False
    print("Where would you like to move to?\n\nType 'nvm' to back out.")
    while not valid_response:
        if isinstance(destination, str):
            response = destination
            destination = None
        else:
            response = input(cursor).lower()
        match response:
            case 'up' | 'north':
                valid_response = my_player.location.up
            case 'down' | 'south':
                valid_response = my_player.location.down
            case 'left' | 'west':
                valid_response = my_player.location.left
            case 'right' | 'east':
                valid_response = my_player.location.right
            case 'in' | 'inside':
                valid_response = my_player.location.inside
            case 'out' | 'outside':
                valid_response = my_player.location.outside
            case 'nevermind' | 'nvm':
                return
        if not valid_response:
            print('\nYou can\'t go that way.\n')
    movement_handler(my_player, valid_response)
            
def movement_handler(my_player, destination):
    os.system('clear')
    player.update_player_location(my_player, location.find_location_by_name(destination).id)
    print(my_player.location.description + '\n')

