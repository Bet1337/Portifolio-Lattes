from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from os import path
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
admin = Admin()

def create_app(): 

    # Configs 
    app = Flask(__name__)
    app.config["SECRET_KEY"] =  "secret"
    app.secret_key = "shhhh e secreto"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    Bootstrap(app)


    db.init_app(app)
    admin.init_app(app)


    #Routes/Views 
    from .routes import views 
    app.register_blueprint(views, url_prefix="/")
    
    #Database
    from . import base
    create_db(app)

    return app

#Create de Database
def create_db(app):
    if not path.exists('lattes_site/database.db'):
        db.create_all(app=app)
        print("Created Database")