import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# User class used to store logined users
class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Category class stores the category in which
# a particular pokemon lies
class Pokemon_Category(Base):

    __tablename__ = 'pokemon_category'
    category = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'category': self.category,
        }


# Pokemon Class stores the data of particular pokemon
class Pokemon(Base):

    __tablename__ = 'pokemon_name'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    img = Column(String(100))
    description = Column(String(500))
    created_by = Column(String(200))
    category_id = Column(Integer, ForeignKey('pokemon_category.id'))
    pokemon_category = relationship(Pokemon_Category)


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'img': self.img,
        }



engine =  create_engine('postgresql://sahil:sahil@localhost/pokemon')

Base.metadata.create_all(engine)
