from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    #to pass values to the template, create and define variables 
    #these variables can be referenced within the template they are 
    #passed to and can be displayed using {{variable_name}} notation within 
    #or outside of blocks 
    #can pass multiple variables, just keep adding them to the list 

    #can also pass boolean variables into the template and write if statements 
    #within the template using the notation:
    #{% if boolean == True %}
    #Yes it is true!
    #{% else %}
    #No it is not true
    #{%endif%}

    #print(data) #ImmutableMultiDict([('email', 'ayesha@gmail.com'), ('password', '123')]) > can access the fields
    #data = request.form #request variable has all the information > method, form attribute, etc 
    #return render_template("login.html", boolean=True)

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #looking based on the users with this email address
        #query the database 
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
                login_user(user, remember=True) #remembers that the user is logged in
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, try again', category='error')
        else:
            flash('User does not exist', category='error')
    return render_template("login.html", user=current_user)
    


@auth.route('/logout')
@login_required   #cannot access this route unless the user is logged in 
def logout():
    logout_user() #helps flask remember that the user was logged out
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["GET", "POST"]) #Defining the http requests that the route can handle 
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already Exists', category='error')
        elif len(email) < 4:
            #can flash a message and group them into categories of your choice
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            #add user to the database 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            #actually creates the new user 
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) #remembers that the user is logged in
            flash('Account Created!', category='success')
            return redirect(url_for('views.home')) #views blueprint, and home method 


    return render_template("sign_up.html", user=current_user)
    