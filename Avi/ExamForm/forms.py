from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,ValidationError,TextAreaField
from wtforms.validators import Length,EqualTo,Email,DataRequired
from ExamForm.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,username_to_check):
        
           user=User.query.filter_by(username=username_to_check.data).first()
           if user:
               raise ValidationError("username already Exits! please try a different username")

    def validate_mobile(self,mobile_to_check):

           mobile=User.query.filter_by(mobile=mobile_to_check.data).first()
           if mobile:
               raise ValidationError("mobile number is alredy registered!! ")
    
    
    username=StringField(label='User Name',validators=[Length(min=2, max=20),DataRequired()])
    Email=StringField(label="Email",validators=[DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    mobile= StringField(label="Mobile Number")
    School=StringField(label="School Name",validators=[DataRequired()])
    submit= SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')