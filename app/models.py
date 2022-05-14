from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Model Class for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=True)
    posts=db.relationship('Post',backref='author',lazy=True)
    comment = db.relationship('Comment', backref='author', lazy='dynamic')


    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)


    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    comment = db.relationship('Comment', backref='post', lazy='dynamic')


    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_id = db.Column(db.Integer,db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment


    def __repr__(self):
        return f'Comment {self.comment}'