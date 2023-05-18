import os, player, location
cursor = "={=======- "

def player_move(my_player, response = None):
    valid_response = False
    nvm = False
    while nvm == False and not valid_response:
        if not response:
            print("Where would you like to move to?\n\nType 'nvm' to back out.")
            response = input(cursor).lower()
            match response:
                case 'up' | 'north':
                    destination = my_player.location.up
                case 'down' | 'south':
                    destination = my_player.location.down
                case 'left' | 'west':
                    destination = my_player.location.left
                case 'right' | 'east':
                    destination = my_player.location.right
                case 'in' | 'inside':
                    destination = my_player.location.inside
                case 'out' | 'outside':
                    destination = my_player.location.outside
                case 'nevermind' | 'nvm':
                    nvm = True
                case _:
                    print('I don\'t know what you mean by that... Try again.')   
    if not nvm:
        movement_handler(my_player, destination)
            
def movement_handler(my_player, destination):
    os.system('clear')
    player.update_location_id(my_player, location.find_by_name(destination).id)
    print(my_player.location.description + '\n')

