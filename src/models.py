import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    rotation_period = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    mass = Column(Integer)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    homeworld_relationship = relationship(Planets)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    model = Column(String(50))
    pilots = Column(Integer, ForeignKey('characters.id'))
    pilots_relationship = relationship(Characters)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

def to_dict(self):
    return {}
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
