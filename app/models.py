from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

#Model Class for User
class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    bio = db.Column(db.String(255))
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'