from models import User

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, user):
    session.add(user)
    session.commit()

def get_all(session):
    return session.query(User).all()

def find_by_name(session, name):
    return session.query(User).filter(User.name == name).first()

def find_by_id(session, id):
    return session.query(User).filter(User.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(User).filter(User.name == name and User.breed == breed).first()

def update_breed(session, user, breed):
    User.breed = breed
    session.add(user)
    session.commit()