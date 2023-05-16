#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Room

if __name__ == '__main__':
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Review).delete()

my_player = User()

a1 = Room(
    name = 'a cave',
    description = '',
    look = 'You peer into the cave and hear a low grumbling.',
    move = '',
    up = 'a2',
    down = '',
    left = '',
    right = 'b1',
)
a2 = Room(
    name = 'an apple orchard',
    description = '',
    look = '',
    move = '',
    up = 'a3',
    down = 'a1',
    left = '',
    right = 'b2',
)
a3 = Room(
    name = 'a natural hot spring',
    description = '',
    look = 'The spring is filled with beautiful maidens.',
    up = '',
    down = 'a2',
    left = '',
    right = 'b3',
)
b1 = Room(
    name = 'a whimsical grove',
    description = 'There\'s a large tree stump on top of the',
    look = '',
    up = 'b2',
    down = '',
    left = 'a1',
    right = '',
)
b2 = Room(
    name = 'a tavern',
    description = 'The village tavern. There\'s a sign above the door reading \'The Drunken Dragon\'.',
    look = '',
    up = 'b3',
    down = 'b1',
    left = 'a2',
    right = 'a3',
)
b3 = Room(
    name = 'the castle gate',
    description = 'The castle is surrounded by a moat.',
    look = 'A knight in shining armor guards the gate',
    up = 'b4',
    down = 'b2',
    left = 'a3',
    right = 'c3',
)
b4 = Room(
    name = 'the throne room',
    description = '',
    look = 'In front of you is a magnificent throne. Atop it lies a golden crown.',
    up = '',
    down = 'b3',
    left = '',
    right = '',
)
c1 = Room(
    name = 'the middle of the lake',
    description = 'It\'s beautiful out here! Apart from the sharks circling your vessel.',
    look = 'You see a faint glimmer directly below your boat.',
    up = 'c2',
    down = '',
    left = '',
    right = '',
)
c2 = Room(
    name = 'a dock',
    description = '',
    look = '',
    up = 'c3',
    down = 'c1',
    left = 'b2',
    right = '',
)
c3 = Room(
    name = 'your lowly farm',
    description = 'a humble cottage next to a field of wheat.',
    look = 'Your house. It ain\'t much but its yours. Thanks to your scarecrow and all the royal shit, the wheat seems to be growing pretty well.',
    up = '',
    down = 'c2',
    left = 'b3',
    right = '',
)
d2 = Room(
    name = '',
    description = '',
    look = '',
    up = '',
    down = '',
    left = '',
    right = '',
)
