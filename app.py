from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from flask_bootstrap import Bootstrap
from forms import AddPet

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# db.create_all()

@app.route('/')
def welcome_page():
    '''Render welcome page and list of current pets.'''
    pets = Pet.query.all()
    print(pets)
    return render_template('welcome.html', pets=pets)

@app.route('/add')
def add_pet_form():
    '''Render add pet form.'''

    form = AddPet()

    return render_template('add_pet_form.html', form=form)
