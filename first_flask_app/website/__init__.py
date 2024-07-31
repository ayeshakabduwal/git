from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hey guys this is for our app'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #importing the blueprints
    from .views import views 
    from .auth import auth 

    #register the blueprints 
    #url prefix just means that no specific route needs to be taken 
    #before the roots are defined in the individual blueprints 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    from .models import User, Note
    
    with app.app_context():
        create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where we go if we are not logged in 
    login_manager.init_app(app) #tells which app we are using 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #tells flask how we load a user 
        #use this function to load a user 


    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')




