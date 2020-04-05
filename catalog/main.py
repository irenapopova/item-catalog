from flask import Flask, render_template, redirect, url_for, session
from db_setup import db_session
from db_setup import Category, Book  # FETCH, define THE CATEGORY OBJECT
from wtforms.ext.sqlalchemy.orm import model_form
from flask_oauth import OAuth
import json
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
# one of the Redirect URIs from Google APIs console

REDIRECT_URI = '/oauth'
# Adding google_client_id
GOOGLE_CLIENT_ID = '803014039877-a673nhe4pvjovn6oldhuf9vfmkrtfddh.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'LQzkXCcqapAZaliVHLqg3W6r'
oauth = OAuth()

# Inititalizing authorization api with Google
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
    books = db_session.query(Book).all()
    # if all passes it is redirected to the actual responce/page

    return render_template("home.html", data=json.loads(res.read()), categories=categories, books=books)

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


# @app.route('/login')
# def login():
#    return render_template("log_in.html")
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
app.secret_key = SECRET_KEY
app.run(host='0.0.0.0', port=8000, debug=True)
# main.py is running the server and
