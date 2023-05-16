#!/usr/bin/env python3

# from sqlalchemy import (Column, String, Integer)
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

class Player:
    def __init__(self):
        self.name = ''
        self.role = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.items = []
        self.location = 'start'
        self.game_over = False

class Room:
    def __init__(self, name, description, look, up, down, left, right):
        self.name = name
        self.description = description
        self.look = look
        self.up = up
        self.down = down
        self.left = left
        self.right = right
    