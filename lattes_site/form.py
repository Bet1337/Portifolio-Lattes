from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length, Email


class Form(FlaskForm): 
    name = StringField('Name:', validators=[DataRequired(),Length(min=4, max=25)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    course =  StringField("Course:", validators=[DataRequired()])
    formation = SelectField('Formation:', choices=['Licenciatura','Bacharel','Mestrado', 'Doutorado'])
    idiom = SelectField('Idioma(Inglês):', choices=['Fluente','Avançado','Intermediário', 'Básico'])    
    address = StringField('Address(City, Street, Number, District):', validators=[DataRequired()])

    