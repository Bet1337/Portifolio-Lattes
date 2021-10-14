from . import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(80), nullable=False)
    formation = db.Column(db.String(80), nullable=False)
    idiom =  db.Column(db.String(80), nullable=False)
    address =  db.Column(db.String(80), nullable=False)

    def __init__(self, name, email, formation, course, idiom, address): 

        self.name = name
        self.email = email
        self.formation = formation
        self.course = course
        self.idiom = idiom 
        self.address = address
