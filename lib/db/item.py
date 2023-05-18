from models import Item, session

def find_item_by_name(name):
    return session.query(Item).filter(Item.name == name).first()

def take_item(player, item):
    item.taken = True
    item.players.append(player)
    session.add(item)
    session.commit()

