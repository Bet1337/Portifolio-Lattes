from flask import Blueprint, render_template, redirect, request, session, flash
from flask.helpers import  url_for
from . import db, admin
from flask_admin.contrib.sqla import ModelView
from lattes_site.base import User
from .form import Form


views =  Blueprint('views', __name__,)


@views.route('/', methods=["GET", "POST"])
def home():
    
    if request.method == "POST": 
        user = request.form["search_form"]
        session["user"] =  user 
        return redirect (url_for("views.user"))

    return render_template('index.html')

@views.route('/register', methods=['GET', 'POST'])
def register():
    forms = Form()
   
    try:
        if forms.validate_on_submit(): 

                user = User(forms.name.data, forms.email.data, forms.formation.data, forms.course.data, forms.idiom.data, forms.address.data)
                db.session.add(user)
                db.session.commit()
                flash("The informations are registred!")
                return redirect("/")
    except:
        flash("Something goes wrong")
        return redirect("/register")

    return render_template('register.html', form=forms)

@views.route('/user')
def user():
    if "user" in session: 
        user = User.query.filter_by(name=session["user"]).first()
        if user:
            return render_template("user.html", user = user)
        return redirect("/") 

admin.add_view(ModelView(User, db.session));