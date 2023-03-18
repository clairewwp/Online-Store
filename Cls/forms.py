from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,TextAreaField
from wtforms.validators import InputRequired, email

class checkout_form(FlaskForm):
    firstname=StringField("First name",validators=[InputRequired()])
    lastname=StringField("Last name",validators=[InputRequired()])
    title=StringField("Title (Miss, Mr, Mrs, Ms)",validators=[InputRequired()])
    phone=StringField("Phone",validators=[InputRequired()])
    email=StringField("Email",validators=[InputRequired(),email()])
    comment=TextAreaField("What do you want to tell us")
    submit=SubmitField("Submit")
    