# this file fills the books data and put them to database
from db_setup import session
from db_setup import Category, Book

# populate the database:

geography = Category(name="Geography")
session.add(geography)
session.commit()

history = Category(name="History")
session.add(history)
session.commit()

computer_science = Category(name="Computer Science")
session.add(computer_science)
session.commit()

history_of_england = Book(
    name="History of England", author="Arthur Dale", category=history.id,)
session.add(history_of_england)
session.commit()
