from flask import Flask, render_template, jsonify
from db_setup import session
from db_setup import Category, Book

app = Flask(__name__)


@app.route('/categories', methods=['GET'])
def get_categories():
    categories = session.query(Category).all()
    data = [i.serialize for i in categories]
    return jsonify(data)


# 1 - 1xx -101,102,120,199 - Information
# 2 - 2xx - 200,201,       - Success
# 3 - 3xx - 301,31         - Redirected
# 4 - 4xx - 400            - client mistake
# 5 - 5xx - 500            - server error

@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    data = [i.serialize for i in books]
    # this generate the json file
    return jsonify(data)

# get books by category id
@app.route('/category/<int:id>', methods=['GET'])
def get_category_by_id(id):
    category = session.query(Category).get(id)
    # this generates json file
    return jsonify(category.serialize)


@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
    books = session.query(Book).get(id)
    return jsonify(books.serialize)


@app.route('/category/<int:id>/books', methods=['GET'])
def get_books_in_category(id):
    books = session.query(Book).all()
    # for -> loop all books
    # filter book which has the same category id
    # make them as json
    data = [book.serialize for book in books if book.category == id]
    return jsonify(data)


if __name__ == "__main__":
    # settings
    app.config["TESTING"] = True
    app.config["FLASK_ENV"] = "development"
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(host='0.0.0.0', port=8000, debug=True)
