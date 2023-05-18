#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Location, Item, Character


if __name__ == '__main__':
    engine = create_engine('sqlite:///game.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Location).delete()
    session.query(Item).delete()
    session.query(Character).delete()

########## Locations ###########
    cave_outside = Location(
        name = 'cave_outside',
        description = 'You come to the mouth of a dark, ominous cave.',
        look = 'You peer into the cave and hear a low grumbling.',
        up = 'orchard',
        right = 'grove',
        inside = 'cave_inside')
    cave_inside = Location(
        name = 'cave_inside',
        description = 'You creep into the cave. A mighty dragon appears out of the darkness. He doesn\'t look happy.',
        look = '',
        outside = 'cave_outside')
    orchard = Location(
        name = 'orchard',
        description = 'You enter an apple orchard. There is a burly lumberjack sitting by one of the apple trees.',
        look = '',
        up = 'spring_outside',
        down = 'cave_outside',
        right = 'tavern_outside',)
    spring_outside = Location(
        name = 'spring_outside',
        description = 'You come across a natural hot spring! It\'s filled to the brim with fair maidens. There doesn\'t seem to be any room for you.',
        look = 'The spring is filled with beautiful maidens.',
        down = 'orchard',
        right = 'castle_outside',
        inside = 'spring_inside')
    spring_inside = Location(
        name = 'spring_inside',
        description = 'Ahhhh. You jump into the spring and feel refreshed. Your stench dissipates.',
        look = 'The spring is filled with beautiful maidens.',
        outside = 'spring_outside')
    grove = Location(
        name = 'grove',
        description = 'You find a whimsical grove. There\'s a gnome sitting atop a large tree stump.',
        look = '',
        up = 'tavern_outside',
        left = 'cave_outside')
    tavern_outside = Location(
        name = 'tavern_outside',
        description = 'You are now outside the village tavern. There\'s a sign above the door reading \'The Drunken Dragon\'.',
        look = '',
        up = 'castle_outside',
        down = 'grove',
        left = 'orchard',
        right = 'dock',
        inside = 'tavern_inside')
    tavern_inside = Location(
        name = 'tavern_inside',
        description = 'You walk in the door. The bartender welcomes you in. A drunken villager sways in the corner of the room.',
        look = '',
        outside = 'tavern_outside')
    castle_outside = Location(
        name = 'castle_outside',
        description = 'You approach the castle gate. It\'s guarded by a knight in shining armor.',
        look = 'A knight in shining armor guards the gate',
        down = 'tavern_outside',
        left = 'spring_outside',
        right = 'home_outside',
        inside = 'castle_inside')
    castle_inside = Location(
        name = 'castle_inside',
        description = 'You walk past the knight into the castle. You are now in the throne room. It\'s BEAUTIFUL.',
        look = 'In front of you is a magnificent throne. Atop it lies a golden crown.',
        outside = 'castle_outside')
    lake = Location(
        name = 'lake',
        description = 'You row the boat out to the middle of the lake. It\'s so nice out here! Apart from the sharks circling your vessel...',
        look = 'You see a faint glimmer directly below your boat.',
        up = 'dock')
    dock = Location(
        name = 'dock',
        description = 'You approach the shore of the lake. A boat floats by the dock.',
        look = '',
        up = 'home_outside',
        down = 'lake',
        left = 'tavern_outside')
    home_outside = Location(
        name = 'home_outside',
        description = 'You\'re outside your house. It ain\'t much but it\'s yours.  Thanks to your scarecrow and all the royal feces, the wheat seems to be growing pretty well.',
        look = '',
        down = 'dock',
        left = 'castle_outside',
        inside = 'home_inside')
    home_inside = Location(
        name = 'home_inside',
        description = 'Home sweet home. It smells of feces.',
        look = 'A map of the town sits on the table.',
        outside = 'home_outside')

    locations = [cave_outside, cave_inside, orchard, spring_outside, spring_inside, grove, tavern_outside, tavern_inside, castle_outside, castle_inside, lake, dock, home_outside, home_inside]
    session.bulk_save_objects(locations)
    session.commit()





########## Items ##########
    sword = Item(
        name = 'sword',
        description = 'It\'s sharp.',
        correct_room_id = 2,
        use = '',
        location_id = 11)
    coin = Item(
        name = 'silver coin',
        description = 'Just enough to buy you a cold one.',
        correct_room_id = 8,
        use = '',
        location_id = 14)
    scarecrow = Item(
        name = 'scarecrow',
        description = 'Could pass as a fair maiden if it had a wig.',
        use = '',
        location_id = 13)
    octopus = Item(
        name = 'octopus',
        description = 'Could be used as a wig',
        use = '',
        location_id = 11)
    fair_maiden = Item(
        name = 'fair maiden',
        description = 'She\'s beautiful!',
        correct_room_id = 9,
        use = '')
    beer = Item(
        name = 'beer',
        description = 'a nice cold flagon of Knightly Keg Crusher IPA.',
        correct_room_id = 2,
        use = '',
        location_id = 8)
    dragon_head = Item(
        name = 'axe',
        description = 'Pretty rusty and dull. Could probably only cut a thin piece of wood.',
        correct_room_id = 9,
        use = '',
        location_id = 7)
    town_map = Item(
        name = 'map',
        description = 'if i look at this, i should see the ascii map.',
        use = '',
        location_id = 14)
    application = Item(
        name = 'king requirements',
        description = 'You must have a fair maiden, slay a foul beast, and not smell like feces.',
        location_id = 14)
    fishing_rod = Item(
        name = 'fishing rod',
        description = 'There\'s already some bait on the hook!',
        correct_room_id = 11,
        use = 'You cast your line into the water.',
        location_id = 12)
    oar = Item(
        name = 'oar',
        description = 'Row row row your boat',
        correct_room_id = 12,
        use = 'You put the oar in the boat. Now you can get to the middle of the lake!',
        location_id = 6)

    items = [oar, sword, coin, scarecrow, octopus, fair_maiden, beer, dragon_head, town_map, application, fishing_rod]
    session.bulk_save_objects(items)
    session.commit()





########## Characters ##########
    knight = Character(
        name = 'knight',
        phrase1 = '',
        phrase2 = '',
        phrase3 = '',
        phrase4= '',
        location_id = 9)
    tavern_keep = Character(
        name = 'tavernkeep',
        phrase1 = 'What can I get ya? We have beer, beer, and beer. One silver coin for a flagon.',
        phrase2 = '',
        phrase3 = '',
        phrase4 = '',
        location_id = 8)
    drunk = Character(
        name = 'drunk guy',
        phrase1 = 'Oh, the Sword of Sunken Lake, a relic of might, Its secrets submerged in the depths of night, A shanty we\'ll sing, with hearts full of lore, Of the blade that lies where the waters roar.',
        phrase2 = 'In a forest deep, where secrets reside, A gnome awaits with riddles to confide, Answer them true, with wit and glee, And he\'ll gift an oar, setting your spirit free.',
        phrase3 = 'In a field so vast, where the wheat does sway, Stands a scarecrow fair, longing for a way, With a wig on its head, it comes to life, A scarecrow\'s heart, as a loving wife.',
        phrase4 = 'In a cavern deep, where flames ignite, A dragon mighty, with scales so bright, But a tankard of ale, its weakness revealed, Pour the brew, and the dragon shall yield.',
        phrase5 = 'By the bubbling spring, with waters pure, A secret lies, a cure so sure, A dragon\'s head, fright in its gaze, Clears the way, the spring\'s cleansing blaze.',
        location_id = 8)
    lumberjack = Character(
        name = 'lumberjack',
        phrase1 = 'ZzzZZzzZzzZ.... Timber... logs... gotta chop... big tree... ZzZzzZz...',
        location_id = 3)
    gnome = Character(
        name = 'gnome',
        phrase1 = 'I have feathers of down, yet never fly, Count me not with your naked eye. On the map I rest, a mystery untold, Pray, dear traveler, how many ducks unfold?',
        phrase2 = 'In this quaint little town, where laughter is found, Where weary souls rest and tales do abound, Where you may drink ale and fall on your face, Pray tell me, dear wanderer, the name of this place?',
        phrase3 = 'No more riddles complex, nor puzzles to claim, I ask but one more question, to know your name.',
        phrase4 = 'now, dear traveler, as a reward for your feat, I present you this oar, a token so sweet.',
        location_id = 6)
    dragon = Character(
        name = 'dragon',
        phrase1 = 'Whhhoooo goeeeessss theeerrre?',
        phrase2 = '',
        phrase3 = '',
        phrase4 = '',
        location_id = 2)
    
    characters = [gnome, dragon, lumberjack, drunk, tavern_keep, knight]
    session.bulk_save_objects(characters)
    session.commit()
    session.close()