from Blog import db
from flask import app
from datetime import datetime
from Blog import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    user=User.query.get(int(user_id))
    return user

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60),nullable=False,unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(140),nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    location=db.Column(db.String(64))
    about_me=db.Column(db.Text())

    def __repr__(self):
        return 'User(%s,%s,%s)' %(self.name,self.email,self.password)


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(240), nullable=False)

    def __repr__(self):
        return 'Post(%s,%s)' %(self.content,self.date_posted)
