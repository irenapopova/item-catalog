from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Categorie

engine = create_engine('sqlite:///new_book_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

Geography = Categorie(name="Geography")
session.add(Geography)
session.commit()