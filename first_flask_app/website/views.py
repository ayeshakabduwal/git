from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

#decorator, and the methods underneath will be run 
#if that route is hit 
@views.route('/', methods=['GET', 'POST'])
@login_required #cannot get to the home page unless we are logged in 
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')



    return render_template("home.html", user=current_user)
    #to render a specific template 
    #this example - renders the home template when the views 
    #home route is hit 

@views.route('delete-note', methods=['POST'])
def delete_note(): 
    data = json.loads(request.data) #takes data from request and loads as python dict  
    noteId = data['noteId'] #access the note id attribute 
    note = Note.query.get(noteId) #find the note in the database 

    if note: #check if the note exists 
        if note.user_id == current_user.id: #if the signed in user owns the note 
            db.session.delete(note) #delete the note 
            db.session.commit()
            
    return jsonify({})

