from flask_wtf import FlaskForm
from wtforms import  StringField , PasswordField,SubmitField,ValidationError
from wtforms.validators import Length , EqualTo , Email , DataRequired,ValidationError
from phat.model import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        user= User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Tên Username đã có người sử dụng!! Xin nhập lại')
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise   ValidationError('Tên mail đã có người sử dụng!! Xin nhập lại')

    username = StringField(label='Username',validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm password',validators = [EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Summit')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password: ', validators=[DataRequired()])
    submit = SubmitField(label='Đăng Nhập')