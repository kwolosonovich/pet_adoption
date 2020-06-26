from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    '''Pet model.'''

    default_image_url = "https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80"
    default_note = "Coming Soon"
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable=False)
    age = db.Column(db.String,
                    nullable=True)
    notes = db.Column(db.String,
                      nullable=False)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
