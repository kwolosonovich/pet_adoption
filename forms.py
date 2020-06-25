from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL

class AddPet(FlaskForm):
    '''Form for adding a pet.'''

    # validators variables
    required = InputRequired()
    url_validator = URL(message='Please provide valid URL')
    optional = Optional()
    photo_validators = [url_validator, optional]

    # form input fields
    name = StringField("Pet's Name", validators=[required])
    species = StringField("Species", validators=[required])
    photo_url = StringField("Photo URL", photo_validators)
    age = FloatField("Age")
    notes = StringField("Notes")