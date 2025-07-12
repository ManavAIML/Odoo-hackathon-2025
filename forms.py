from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', false_values=('false', 'False', '0', 0))
    submit = SubmitField('Login')

class AddItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    type = StringField('Type/Style')
    size = RadioField('Size', choices=[('S','S'), ('M','M'), ('L','L'), ('XL','XL'), ('XXL','XXL')], validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    tags = StringField('Tags')
    submit = SubmitField('List Item')
