# this file create the empty database
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import randint
Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    # we need a primary key for every Bases
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

# create a relation between book and category


class Book(Base):
    __tablename__ = 'book'
    # we need a primary key for every Bases
    id = Column(Integer, primary_key=True)
    category = Column(Integer, ForeignKey('category.id'))
    name = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    # the price column should have a value
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=False)
    image = Column(String(300), nullable=False)

    def __init__(self):
        self.id = id
        self.category = category
        self.name = name
        self.author = author
        self.price = price
        self.description = description
        self.image = image

    def __init__(self, id, category, name, author, price, description, image):
        self.id = id
        self.category = category
        self.name = name
        self.author = author
        self.price = price
        self.description = description
        self.image = image

    @property
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'author': self.author,
            'price': self.price,
            'description': self.description,
            'image': self.image
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)

    def __init__(self):
        self.id = id
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, nullable=False)
    book = Column(Integer, ForeignKey("book.id"))

    def __init__(self, user_id, book_id):
        self.user = user_id
        self.book = book_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user': self.user
        }


engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()
