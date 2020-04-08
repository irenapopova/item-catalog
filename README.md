## Item Catalog Project

### Full Stack Web Developer Nanodegree program virtual machine

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

Virtual machine for the [Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197) and [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088) courses in the [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

#### My Second project

#### Technologies used
Python
Flask
Flask-Bootstrap
HTML,CSS and JS


#### About

An application with catalog functionality. <br/><br/>
This application provides a list of items(Books) within a variety of **categories** as well as provide a user authentication system using google APIS instead of in house.

Registered users will have the ability to post, edit, and delete their own items(books) and also can store their favorites for future.

#### Project Structure (the tree)
```
catalog
├── README.txt
├── api
├── api.py
├── db.db
├── db.db-journal
├── db_setup.py
├── db_setup.pyc
├── forms.py
├── forms.pyc
├── js
│   └── app.js
├── main.py
├── populate_data.py
├── requirements.txt
├── static
│   └── style.css
└── templates
    ├── _formhelpers.html
    ├── book.html
    ├── bookDetail.html
    ├── book_create.html
    ├── category.html
    ├── category_create.html
    ├── editBook.html
    ├── fav.html
    ├── genres.html
    ├── home.htm.bkpl
    ├── home.html
    ├── index.html
    ├── log_in.html
    ├── newBook.html
    └── signin.html
```
#### Steps to run this project

clone the project
run in project file in terminal :

- `pip install -r requirements.txt`
- `cd catalog`
- `python main.py`
- open `http://127.0.0.1:8000/`
