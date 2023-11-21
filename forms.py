from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, Regexp


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    fullname = StringField("Fullname", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    phone_number = IntegerField("Phone Number", validators=[DataRequired(),Length(min=10, max=10),Regexp(regex='^[+-]?[0-9]$')])
    upline = StringField("Upline")
    coupon = StringField("Coupon Code", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    tandc = RadioField("Terms", choices=[("true", "I have read and agreed to the terms and congitions")])
    submit = SubmitField("Register")


class CouponCheckForm(FlaskForm):
    coupon = StringField("Coupon", validators=[DataRequired()])
    submit = SubmitField()
