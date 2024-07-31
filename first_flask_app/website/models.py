from . import db  #imports the db object from init_py in the package 
from flask_login import UserMixin
from sqlalchemy.sql import func

#by default, don't need to define, database software increments it


#note model: sql alchemy handles setting the date and time
#by getting it from func.now
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    #foreign key to reference the id to another database column 
    #one to many relationship > ref id field from user object 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



#defines the user model 
class User(db.Model, UserMixin):
    #creates column, integer is the
    #type of columnn and this is the primary key 
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(150), unique=True) #no same email, 150 char string 
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    #every time we make a note, add the noteid to the relationship (list)
    notes = db.relationship('Note') 

 
