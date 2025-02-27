from flask import app, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message:', validators=[InputRequired()])
    submit = SubmitField('Send')