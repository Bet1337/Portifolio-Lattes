from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length, Email


class Form(FlaskForm): 
    name = StringField('Nome:', validators=[DataRequired(),Length(min=4, max=25)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    course =  StringField("Curso:", validators=[DataRequired()])
    formation = SelectField('Formação:', choices=['Licenciatura','Bacharel','Mestrado', 'Doutorado'])
    idiom = SelectField('Idioma(Inglês):', choices=['Fluente','Avançado','Intermediário', 'Básico'])    
    address = StringField('Endereço(Cidade, Rua, Número, Bairro):', validators=[DataRequired()])


