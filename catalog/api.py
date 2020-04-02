from flask import Flask, render_template, jsonify
from db_setup import session
from db_setup import Category, Book

app = Flask(__name__)


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = session.query(Category).all()
    data = [i.serialize for i in categories]
    return jsonify(data)


@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    data = [i.serialize for i in books]
    return jsonify(data)

# get books by category id
@app.route('/category/<int:id>', methods=['GET'])
def get_category_by_id(id):
    category = session.query(Category).get(id)
    return jsonify(category.serialize)


@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
    books = session.query(Book).get(id)

    return jsonify(books.serialize)


if __name__ == "__main__":
    # settings
    app.config["TESTING"] = True
    app.config["FLASK_ENV"] = "development"
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(host='0.0.0.0', port=8000, debug=True)
