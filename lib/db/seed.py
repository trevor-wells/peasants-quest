#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Location, Item, Character, Player


if __name__ == '__main__':
    engine = create_engine('sqlite:///game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Player).delete()
    session.query(Location).delete()
    session.query(Item).delete()
    session.query(Character).delete()

########## Locations ###########
    cave_outside = Location(
        name = 'cave_outside',
        description = 'You stand at the mouth of a dark, ominous cave. You can hear a low grumbling coming from deep inside.',
        look = '',
        up = 'orchard',
        right = 'mushroom_outside',
        inside = 'cave_inside')
    cave_inside = Location(
        name = 'cave_inside',
        description = 'You venture into the cave.',
        look = '',
        outside = 'cave_outside')
    orchard = Location(
        name = 'orchard',
        description = 'You stand in the middle of an apple orchard.',
        look = '',
        up = 'spring_outside',
        down = 'cave_outside',
        right = 'tavern_outside',)
    spring_outside = Location(
        name = 'spring_outside',
        description = 'You stand on the bank of a natural hot spring. It\'s filled to the brim with fair maidens. There doesn\'t seem to be any room for you.',
        look = '',
        down = 'orchard',
        right = 'castle_outside',
        inside = 'spring_inside')
    spring_inside = Location(
        name = 'spring_inside',
        description = 'You jump into the spring and feel refreshed. Your stench dissipates.',
        look = '',
        outside = 'spring_outside')
    mushroom_outside = Location(
        name = 'mushroom_outside',
        description = 'You stand in a whimsical grove. There\'s a house made of mushroom in the clearing.',
        look = '',
        up = 'tavern_outside',
        left = 'cave_outside',
        inside = 'mushroom_inside')
    tavern_outside = Location(
        name = 'tavern_outside',
        description = 'You stand at the center of the village. In front of you stands a tavern. There\'s a sign above the door reading \'The Drunken Dragon\'.',
        look = '',
        up = 'castle_outside',
        down = 'mushroom_outside',
        left = 'orchard',
        right = 'dock',
        inside = 'tavern_inside')
    tavern_inside = Location(
        name = 'tavern_inside',
        description = 'You walk in the door to the tavern.',
        look = '',
        outside = 'tavern_outside')
    castle_outside = Location(
        name = 'castle_outside',
        description = 'You stand in front of the castle gate.',
        look = 'A knight in shining armor guards the gate',
        down = 'tavern_outside',
        left = 'spring_outside',
        right = 'home_outside',
        inside = 'castle_inside')
    castle_inside = Location(
        name = 'castle_inside',
        description = 'After showing the knight your completed King application, he hands you the royal crown.',
        look = 'In front of you is a magnificent throne. Atop it lies a golden crown.',
        outside = 'castle_outside')
    lake = Location(
        name = 'lake',
        description = 'You row the boat out to the middle of the lake. It\'s so nice out here! Apart from the sharks circling your vessel...',
        look = 'You see a faint glimmer directly below your boat.',
        up = 'dock')
    dock = Location(
        name = 'dock',
        description = 'You stand on the north shore of the lake. A small wooden boat floats by the dock.',
        look = '',
        up = 'home_outside',
        down = 'lake',
        left = 'tavern_outside')
    home_outside = Location(
        name = 'home_outside',
        description = 'You stand outside your humble wheat farm. Thanks to the castle\'s sewage system spewing royal excrement right on your property, the wheat seems to be growing pretty well.',
        look = '',
        down = 'dock',
        left = 'castle_outside',
        inside = 'home_inside')
    home_inside = Location(
        name = 'home_inside',
        description = 'Home sweet home. It smells of feces.',
        look = 'A map of the town sits on the table.',
        outside = 'home_outside')
    mushroom_inside = Location(
        name = 'mushroom_inside',
        description = 'You enter the mushroom house.',
        look = '',
        outside = 'mushroom_outside')

    locations = [cave_outside, cave_inside, orchard, spring_outside, spring_inside, mushroom_outside, tavern_outside, tavern_inside, castle_outside, castle_inside, lake, dock, home_outside, home_inside, mushroom_inside]
    session.bulk_save_objects(locations)
    session.commit()





########## Items ##########
    sword = Item(
        name = 'sword',
        description = 'A faint golden glimmer can be seen at the very bottom of the lake.',
        correct_room_id = 2,
        use = '',
        location_id = 11)
    coin = Item(
        name = 'coin',
        description = 'One of the maidens holds a silver coin in her hand. She offers to buy food from you if you have any.',
        correct_room_id = 8,
        use = '',
        location_id = 4)
    apple = Item(
        name ='apple',
        description = 'A juicy red apple hangs from a low branch.',
        correct_room_id = 4,
        use = '',
        location_id = 3)
    scarecrow = Item(
        name = 'scarecrow',
        description = 'A scarecrow stands in the middle of your wheat field. The stick that holds him up is starting to rot.',
        use = '',
        location_id = 13)
    octopus = Item(
        name = 'octopus',
        description = 'An octopus swims directly under your boat.',
        use = '',
        location_id = 11)
    fair_maiden = Item(
        name = 'fair maiden',
        description = 'You shouldn\'t be able to pick up the "fair maiden", but because I have not yet programmed the ability to combine your items, here she is.',
        correct_room_id = 9,
        use = '',
        location_id = 7)
    beer = Item(
        name = 'beer',
        description = 'A nice cold flagon of Knightly Keg Crusher IPA sits on the bar.',
        correct_room_id = 2,
        use = '',
        location_id = 8)
    axe = Item(
        name = 'axe',
        description = 'A rusty axe rests in the lumberjack\'s hands.',
        correct_room_id = 9,
        use = '',
        location_id = 7)
    dragon_head = Item(
        name = 'dragon head',
        description = 'The dragon\'s severed head rests on the floor of the cave. It\'s really gross.',
        correct_room_id = 9,
        use = '',
        location_id = 2)
    town_map = Item(
        name = 'map',
        description = 'You see a map of the town on the table.',
        use = '',
        location_id = 14)
    application = Item(
        name = 'application',
        description = 'The application is laying on the floor in front of your door.',
        location_id = 14)
    fishing_rod = Item(
        name = 'fishing rod',
        description = 'A fishing rod lies on the dock. It\'s already got some bait on the hook!',
        correct_room_id = 11,
        use = 'You cast your line into the water.',
        location_id = 12)
    oar = Item(
        name = 'oar',
        description = 'The gnome holds a large wooden oar in his hands.',
        correct_room_id = 12,
        use = 'You put the oar in the boat. Now you can get to the middle of the lake!',
        location_id = 15)

    items = [oar, sword, coin, apple, scarecrow, octopus, fair_maiden, beer, town_map, application, fishing_rod]
    session.bulk_save_objects(items)
    session.commit()





########## Characters ##########
    knight = Character(
        name = 'knight',
        description = 'A knight in shining armor guards the gate to the castle.',
        phrase1 = 'Halt! No entry to the castle unless you have a completed application.',
        phrase2 = '',
        phrase3 = '',
        phrase4= '',
        location_id = 9)
    tavern_keep = Character(
        name = 'tavernkeep',
        description = 'The tavernkeep stands behind the bar.',
        phrase1 = 'What can I get ya? We have beer, beer, and beer. One silver coin for a flagon.',
        phrase2 = '',
        phrase3 = '',
        phrase4 = '',
        location_id = 8)
    drunk = Character(
        name = 'drunk guy',
        description = 'A drunk guy sways in the corner of the room.',
        phrase1 = 'Oh, the Sword of Sunken Lake, a relic of might, Its secrets submerged in the depths of night, A shanty we\'ll sing, with hearts full of lore, Of the blade that lies where the waters roar.',
        phrase2 = 'In a forest deep, where secrets reside, A gnome awaits with riddles to confide, Answer them true, with wit and glee, And he\'ll gift an oar, setting your spirit free.',
        phrase3 = 'In a field so vast, where the wheat does sway, Stands a scarecrow fair, longing for a way, With a wig on its head, it comes to life, A scarecrow\'s heart, as a loving wife.',
        phrase4 = 'In a cavern deep, where flames ignite, A dragon mighty, with scales so bright, But a tankard of ale, its weakness revealed, Pour the brew, and the dragon shall yield.',
        phrase5 = 'By the bubbling spring, with waters pure, A secret lies, a cure so sure, A dragon\'s head, fright in its gaze, Clears the way, the spring\'s cleansing blaze.',
        location_id = 8)
    lumberjack = Character(
        name = 'lumberjack',
        description = 'A burly lumberjack sleeps against the trunk of one of the apple trees.',
        phrase1 = 'ZzzZZzzZzzZ.... Timber... logs... gotta chop... big tree... ZzZzzZz...',
        location_id = 3)
    gnome = Character(
        name = 'gnome',
        description = 'A gnome sits in the middle of the room.',
        phrase1 = 'I have feathers of down, yet never fly, Count me not with your naked eye. On the map I rest, a mystery untold, Pray, dear traveler, how many ducks unfold?',
        phrase2 = 'In this quaint little town, where laughter is found, Where weary souls rest and tales do abound, Where you may drink ale and fall on your face, Pray tell me, dear wanderer, the name of this place?',
        phrase3 = 'No more riddles complex, nor puzzles to claim, I ask but one more question, to know your name.',
        phrase4 = 'now, dear traveler, as a reward for your feat, I present you this oar, a token so sweet.',
        location_id = 15)
    dragon = Character(
        name = 'dragon',
        description = 'A mighty dragon appears from the darkness. He doesn\'t seem happy.',
        phrase1 = 'Whhhoooo goeeeessss theeerrre?',
        phrase2 = '',
        phrase3 = '',
        phrase4 = '',
        location_id = 2)
    
    characters = [gnome, dragon, lumberjack, drunk, tavern_keep, knight]
    session.bulk_save_objects(characters)
    session.commit()
    session.close()