from flask import Blueprint, render_template, redirect, request, session
from flask.helpers import  url_for
from . import db
from lattes_site.base import User
from .form import Form, Search


views =  Blueprint('views', __name__,)

def user_search(): 
     search = request.args.get("search_form")
     return (User.query.filter_by(name=search).first())


@views.route('/', methods=["GET", "POST"])
def home():
    
    return render_template('index.html')

@views.route('/register', methods=['GET', 'POST'])
def register():
    forms = Form()
   
    user = user_search()
    if user:
        session["user"] =  user.name
        return redirect(url_for("views.user"))

    if forms.validate_on_submit(): 
        user = User(forms.name.data, forms.email.data, forms.formation.data, forms.abstract.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/") #Ajustar a validação

    return render_template('register.html', form=forms)

@views.route('/user')
def user():
    if "user" in session: 
        user = User.query.filter_by(name=session["user"]).first()
        return render_template("user.html", usr= user)
