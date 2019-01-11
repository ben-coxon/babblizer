

from flask_wtf import Form
from wtforms import StringField, BooleanField, FileField, HiddenField
from wtforms.validators import DataRequired
from flask import request

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class DemoForm(Form):
    build = StringField('demo',validators=[DataRequired()])

class AddForm(Form):
    yousay = StringField('yousay', validators=[DataRequired()])
    isay = StringField('isay', validators=[DataRequired()])
