#!/usr/bin/env python3

from sqlalchemy import create_engine, Table, ForeignKey, Column, String, Integer, Boolean, MetaData
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",}
metadata = MetaData(naming_convention = convention)

Base = declarative_base(metadata = metadata)
engine = create_engine('sqlite:///game.db')
Session = sessionmaker(bind=engine)
session = Session()

player_item = Table(
    'player_items',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('player_id', ForeignKey('players.id')),
    Column('item_id', ForeignKey('items.id')),
    extend_existing=True)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key = True)
    name = Column(String())

    location_id = Column(Integer(), ForeignKey('locations.id'))
    items = relationship('Item', secondary=player_item, back_populates='players')

    def __repr__(self):
        return f'Player {self.id}'

class Location(Base):
    __tablename__ = 'locations'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())
    look = Column(String())
    up = Column(String())
    down = Column(String())
    left = Column(String())
    right = Column(String())
    outside = Column(String())
    inside = Column(String())

    players = relationship('Player', backref=backref('location'))
    items = relationship('Item', backref=backref('location'))
    characters = relationship('Character', backref=backref('location'))
    
    def __repr__(self):
        return f'Location {self.id}: {self.name}'

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())
    use = Column(String())
    correct_room_id = Column(Integer())

    location_id = Column(Integer(), ForeignKey('locations.id'))
    players = relationship('Player', secondary = player_item, back_populates = 'items')

    def __repr__(self):
        return f'Item {self.id}: {self.name}'
    
class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phrase1 = Column(String())
    phrase2 = Column(String())
    phrase3 = Column(String())
    phrase4 = Column(String())
    phrase5 = Column(String())
    phrase6 = Column(String())

    location_id = Column(Integer(), ForeignKey('locations.id'))

    def __repr__(self):
        return f'Character {self.id}: {self.name}'
    
