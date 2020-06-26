from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPet(FlaskForm):
    '''Form for adding a pet.'''

    # validators variables
    required = InputRequired()
    url_validator = URL(message='Please provide valid URL')
    optional = Optional(strip_whitespace=True)
    photo_validators = [url_validator, optional]
    num_validator = NumberRange(min=0, max=30, message="Please provide pet's age")
    age_validators = [num_validator, optional]

    # form input fields
    name = StringField("Pet's Name", validators=[required])
    species = SelectField(u'Species', choices=[('dog', 'Dog'),
                                               ('cat', 'Cat'),
                                               ('porcupine', 'Porcupine')],
                          validators=[required])
    photo_url = StringField("Photo URL", validators=photo_validators)
    age = IntegerField("Age", validators=age_validators)
    notes = StringField("Notes")
