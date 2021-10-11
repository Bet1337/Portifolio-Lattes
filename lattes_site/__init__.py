from flask import Flask
from flask.helpers import url_for 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(): 

    app = Flask(__name__)
    app.config["SECRET_KEY"] =  "secret"
    app.secret_key = "shhhh e secreto"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
    Bootstrap(app)

    #Routes/Views 
    from .routes import views 
    app.register_blueprint(views, url_prefix="/")
    
    #Database
    from . import base
    create_db(app)

    return app

def create_db(app):
    if not path.exists('lattes_site/database.db'):
        db.create_all(app=app)
        print("Created Database")