from models import Character, session

def find_character_by_name(name):
    my_character = session.query(Character).filter(Character.name == name).first()
    return my_character