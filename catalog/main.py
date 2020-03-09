from flask import Flask, render_template
from db_setup import session
from db_setup import Category, Book  # FETCH, define THE CATEGORY OBJECT
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''

    # User is the name of table that has a column name
    categories = session.query(Category).all()
    books = session.query(Book).all()

    return render_template("index.html", categories=categories, books=books)


@app.route('/login')
def login():
    return render_template("log_in.html")
    # return "<div class='login'>Login</div>"


@app.route('/categories/<id>')  # the id is the named parameter in the url_for
def category_detail(id):
    return render_template("category.html", id=id)


@app.route('/books/<id>')  # the id is the named parameter in the url_for
def book_detail(id):
    return render_template("book.html", id=id)
# fetches the data


BookForm = model_form(Book)
@app.route('/books/<id>/edit')  # the id is the named parameter in the url_for
def edit_book(id):
    pass  # do nothing simply continue

# render turn into html


app.config["TESTING"] = True
app.config["FLASK_ENV"] = "development"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.run(host='0.0.0.0', port=8000, debug=True)
# main.py is running the server and
