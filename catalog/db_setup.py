# this file create the empty database
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    # we need a primary key for every Bases
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("user.id"))
    book = Column(Integer, ForeignKey("book.id"))


engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
