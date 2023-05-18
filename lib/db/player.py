from models import Player, session

def give_player_name(player, name):
    player.name = name
    session.add(player)
    session.commit()

def find_player_by_name(name):
    my_player = session.query(Player).filter(Player.name == name).first()
    if not my_player:
        my_player = Player(
        name = name,
        location_id = 14)
        session.add(my_player)
        session.commit()
    return my_player

def get_all_players():
    return session.query(Player).all()

def update_player_location(player, new_id):
    player.location_id = new_id
    session.add(player)
    session.commit()

def delete_player(player):
    session.delete(player)
    session.commit()

