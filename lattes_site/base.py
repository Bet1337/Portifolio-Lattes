from . import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    formation = db.Column(db.String(80), nullable=False)
    abstract =  db.Column(db.String(300), nullable=False)

    def __init__(self, name, email, formation, abstract): 

        self.name = name
        self.email = email
        self.formation = formation
        self.abstract = abstract