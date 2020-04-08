from flask import Flask, render_template, redirect, url_for, session, request
from db_setup import db_session
# FETCH, define THE CATEGORY OBJECT
from db_setup import Category, Book, Favorite
from wtforms.ext.sqlalchemy.orm import model_form
from flask_oauth import OAuth
import json
from flask_bootstrap import Bootstrap
from forms import CategoryForm, BookForm
from random import randint

app = Flask(__name__)
Bootstrap(app)
# one of the Redirect URIs from Google APIs console

REDIRECT_URI = '/oauth'
# Adding google_client_id
GOOGLE_CLIENT_ID = '803014039877-a673nhe4pvjovn6oldhuf9vfmkrtfddh.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'LQzkXCcqapAZaliVHLqg3W6r'
oauth = OAuth()

# Initializing authorization api with Google
google = oauth.remote_app('google', base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth', request_token_url=None, request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email', 'response_type': 'code'}, access_token_url='https://accounts.google.com/o/oauth2/token', access_token_method='POST', access_token_params={'grant_type': 'authorization_code'}, consumer_key=GOOGLE_CLIENT_ID, consumer_secret=GOOGLE_CLIENT_SECRET)
SECRET_KEY = 'development key'
##
@app.route('/home')
def index():
    # check if token is avaliable
    access_token = session.get('access_token')
    if access_token is None:
        # if token is not there redirect user to login page
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request(
        'https://www.googleapis.com/oauth2/v1/userinfo', None, headers)
    try:
        res = urlopen(req)
    except URLError as e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)  # delete the existing token
            return redirect(url_for('login'))  # redirect to login page

    # fetch all categories
    categories = db_session.query(Category).all()
    # check if url is called with category id
    category_id = request.args.get("id")
    books = db_session.query(Book).all()
    # check if category id is provided in url
    # print(len(books))
    # print(category_id)
    if category_id is not None:
        # print("i am inside "+str(category_id))
        books = [book for book in books if book.category == int(category_id)]
       # print(len(books))
    # if all passes it is redirected to the actual responce/page

    # get favortiees of the user
    all_fav = db_session.query(Favorite).all()
    # 123:456
    my_fav = [str(fav.book)+":"+str(fav.user) for fav in all_fav]
    return render_template("home.html", data=json.loads(res.read()), categories=categories, books=books, fav=my_fav)

# l user calls login  url should be redirected to google for authorize
@app.route('/login')
def login():
    callback = url_for('authorized', _external=True)
    # ask google to authorize the userinformation
    return google.authorize(callback=callback)


@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    # google will call me back and then provide me access_token
    access_token = resp['access_token']
    # putting token in browser and can be reused many time
    session['access_token'] = access_token, ''
    # proceed to index page
    return redirect(url_for('index'))


@google.tokengetter
def get_access_token():
    # save token in session to reuse many time
    return session.get('access_token')


@app.route('/fav')
def fav():
    user_id = request.args.get("user")[:5]
    all_fav = db_session.query(Favorite).all()
    my_fav_books = [fav.book for fav in all_fav if int(fav.user) == int(user_id)]
    print(my_fav_books)
    books_list = db_session.query(Book).filter(Book.id.in_(tuple(my_fav_books))).all()
    return render_template("fav.html",books=books_list)
    # return "<div class='login'>Login</div>"


@app.route("/create_fav")
def create_fav():
    user_id = request.args.get("user_id")
    book_id = request.args.get("book_id")
    favorite = Favorite(user_id, book_id)
    db_session.add(favorite)
    return redirect("/home")


@app.route('/categories/<id>')  # the id is the named parameter in the url_for
def category_detail(id):
    return render_template("category.html", id=id)


@app.route('/books/<id>')  # the id is the named parameter in the url_for
def book_detail(id):
    return render_template("book.html", id=id)
# fetches the data


# BookForm = model_form(Book)
@app.route('/books/<id>/edit')  # the id is the named parameter in the url_for
def edit_book(id):
    pass  # do nothing simply continue

# render turn into html

# remove session token from google and then redirect to anonymous
@app.route("/logout")
def logout():
    session.pop('access_token', None)
    return redirect("/")


@app.route('/')
def anonymous():
    categories = db_session.query(Category).all()
    # check if url is called with category id
    category_id = request.args.get("id")
    books = db_session.query(Book).all()
    # check if category id is provided in url
    if category_id is not None:
        books = [book for book in books if book.category == int(category_id)]
    # if all passes it is redirected to the actual responce/page
    return render_template("home.html", data={}, categories=categories, books=books)


@app.route('/category', methods=['GET', 'POST'])
def register():
    form = CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        # auto generate category id in betwen 10 - 20000
        category = Category(randint(10, 20000), form.name.data)
        db_session.add(category)
        return redirect('/home')
    return render_template('category_create.html', form=form)


@app.route('/book', methods=['GET', 'POST'])
def book():
    form = BookForm(request.form)
    print(form)
    catgories = db_session.query(Category).all()
    # create category list
    catgories_list = [(category.id, category.name) for category in catgories]
    form.category.choices = catgories_list
    if request.method == 'POST' and form.validate():
        # auto generate category id in bettwen 10 - 20000
        book = Book(randint(10, 20000),
                    form.category.data, form.name.data, form.author.data, form.price.data, form.description.data, form.image.data)
        db_session.add(book)
        return redirect('/home')
    return render_template('book_create.html', form=form)


app.config["TESTING"] = True
app.config["FLASK_ENV"] = "development"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = SECRET_KEY
app.run(host='0.0.0.0', port=8000, debug=True)
# main.py is running the server and
