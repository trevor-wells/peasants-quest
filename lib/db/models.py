#!/usr/bin/env python3

from sqlalchemy import Table, ForeignKey, Column, String, Integer, Boolean, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",}
metadata = MetaData(naming_convention = convention)

Base = declarative_base(metadata = metadata)

player_item = Table(
    'player_items',
    Base.metadata,
    Column('id', Integer(), primary_key = True),
    Column('player_id', ForeignKey('players.id'), primary_key = True),
    Column('item_id', ForeignKey('items.id'), primary_key = True),
    extend_existing = True
)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key = True)
    dead = Column(Boolean())

    location_id = Column(Integer(), ForeignKey('locations.id'))
    items = relationship('Item', secondary = player_item, back_populates = 'players')

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
    
    def __repr__(self):
        return f'Location {self.id}: {self.name}'

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())

    location_id = Column(Integer(), ForeignKey('locations.id'))
    players = relationship('Player', secondary = player_item, back_populates = 'items')

    def __repr__(self):
        return f'Item {self.id}: {self.name}'