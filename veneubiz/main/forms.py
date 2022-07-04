import flask_login
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,NumberRange
from venuebiz.models import user ,Venue
from flask_login import current_user




class Contact(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone=StringField("phone number", validators=[DataRequired(), Length(10)])
    query=TextAreaField('Description',
                           validators=[DataRequired(),Length(min=50, max=200)])

    submit = SubmitField('submit')
    