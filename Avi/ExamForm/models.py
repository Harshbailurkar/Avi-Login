from ExamForm import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from ExamForm import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    phoneNo = db.Column(db.Integer(), nullable=False, unique=True)
    Password = db.Column(db.String(length=60), nullable=False)
    School = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.Password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_passward):
        return bcrypt.check_password_hash(self.Password, attempted_passward)

    def __repr__(self):
        return f'User{self.name}'