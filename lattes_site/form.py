from typing import AbstractSet
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class Form(FlaskForm): 
    name = StringField('Name', validators=[DataRequired(),Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired()])
    formation = SelectField('Formation', choices=['Licenciatura','Bacharel','Mestrado', 'Doutorado'])
    abstract =  TextAreaField("Abstract", validators=[DataRequired(), Length(max=300)])

class Search(FlaskForm):
    search = StringField("Search")
    
