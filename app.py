from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from flask_bootstrap import Bootstrap
from forms import AddPet
from seed import seed_database

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

seed_database()


@app.route('/')
def welcome_page():
    '''Render welcome page and list of current pets.'''
    pets = Pet.query.all()
    return render_template('welcome.html', pets=pets)


@app.route('/add', methods=['POST', 'GET'])
def add_pet_form():
    '''Render add pet form.'''

    form = AddPet()

    if form.validate_on_submit():
        print('form validated')
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if len(photo_url) == 0 or photo_url is None:
            photo_url = Pet.default_image_url
        age = form.age.data
        notes = form.notes.data
        if len(notes) == 0 or notes is None:
            notes = Pet.default_note
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/edit/<pet_id>', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    print(pet_id)
    '''Render edit pet form and pet details.'''
    pet = Pet.query.get_or_404(pet_id)
    form = AddPet(obj=pet)
    return render_template('edit_pet_form.html', form=form, pet=pet)
