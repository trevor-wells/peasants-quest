#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Location

if __name__ == '__main__':
    engine = create_engine('sqlite:///game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Player).delete()
    session.query(Location).delete()

    cave_outside = Location(
        name = 'a cave',
        description = '',
        look = 'You peer into the cave and hear a low grumbling.',
        up = 'orchard',
        right = 'grove',
        inside = 'cave_inside')
    cave_inside = Location(
        name = 'inside the cave',
        description = '',
        look = '',
        outside = 'cave_outside')
    orchard = Location(
        name = 'an apple orchard',
        description = '',
        look = '',
        up = 'spring',
        down = 'cave_outside',
        right = 'tavern',)
    spring_outside = Location(
        name = 'outside a natural hot spring',
        description = '',
        look = 'The spring is filled with beautiful maidens.',
        down = 'orchard',
        right = 'castle_outside',)
    spring_inside = Location(
        name = 'a natural hot spring',
        description = '',
        look = 'The spring is filled with beautiful maidens.',
        outside = 'spring_outside')
    grove = Location(
        name = 'a whimsical grove',
        description = 'There\'s a large tree stump on top of the',
        look = '',
        up = 'tavern',
        left = 'cave')
    tavern_outside = Location(
        name = 'outside a tavern',
        description = 'The village tavern. There\'s a sign above the door reading \'The Drunken Dragon\'.',
        look = '',
        up = 'castle_outside',
        down = 'grove',
        left = 'orchard',
        right = 'dock')
    tavern_inside = Location(
        name = 'inside the tavern',
        description = '',
        look = '',
        outside = 'tavern_outside')
    castle_outside = Location(
        name = 'the castle gate',
        description = 'The castle is surrounded by a moat.',
        look = 'A knight in shining armor guards the gate',
        down = 'tavern',
        left = 'spring',
        right = 'home_outside',
        inside = 'castle_inside')
    castle_inside = Location(
        name = 'the throne Location',
        description = '',
        look = 'In front of you is a magnificent throne. Atop it lies a golden crown.',
        outside = 'castle_outside')
    lake = Location(
        name = 'the middle of the lake',
        description = 'It\'s beautiful out here! Apart from the sharks circling your vessel.',
        look = 'You see a faint glimmer directly below your boat.',
        up = 'dock')
    dock = Location(
        name = 'a dock',
        description = '',
        look = '',
        up = 'home_outside',
        down = 'lake',
        left = 'tavern_outside')
    home_outside = Location(
        name = 'your lowly farm',
        description = 'a humble cottage next to a field of wheat.',
        look = 'Your house. It ain\'t much but its yours. Thanks to your scarecrow and all the royal feces, the wheat seems to be growing pretty well.',
        down = 'dock',
        left = 'castle_outside',
        inside = 'home_inside')
    home_inside = Location(
        name = 'inside your house',
        description = 'It smells like feces.',
        look = 'A map of the town sits on the table.',
        outside = 'home_outside')

    my_player = Player(dead = False)
    
    locations = [my_player, cave_outside, cave_inside, orchard, spring_outside, spring_inside, grove, tavern_outside, tavern_inside, castle_outside, castle_inside, lake, dock, home_outside, home_inside]
    session.add(my_player)
    session.bulk_save_objects(locations)
    session.commit()
    session.close()