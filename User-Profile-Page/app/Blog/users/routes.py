from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required
from Blog.users.forms import PostForm,EditForm
from Blog.models import User,Post
from flask_login import current_user
from Blog import db


users=Blueprint('users',__name__)



@users.route('/home/',methods=['GET','POST'])
@login_required
def index():
    form=PostForm()
    if form.validate_on_submit():
        post=Post(content=form.content.data ,author=current_user)
        db.session.add(post)
        db.session.commit()
        form.content.data=''
    return render_template('index.html',form=form)

@users.route('/profile/<string:username>')
def profile(username):
    form=EditForm()
    user=User.query.filter_by(username=username).first()
    post=Post.query.all()
    return render_template('profile.html',user=user,post=post,form=form)

@users.route('/edit/<string:username>')
def edit(username):
    user=User.query.filter_by(username=username).first()
    return render_template('edit.html',user=user)
