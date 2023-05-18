from models import Location, session

def find_location_by_name(name):
    return session.query(Location).filter(Location.name == name).first()

def find_location_by_id(id):
    return session.query(Location).filter(Location.id == id).first()

