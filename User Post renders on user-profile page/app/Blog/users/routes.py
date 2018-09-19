from flask import Blueprint,render_template,redirect,url_for,flash,request
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

@users.route('/profile/<string:username>',methods=['GET','POST'])
@login_required
def profile(username):
    form=EditForm()
    user=User.query.filter_by(username=username).first()
    post=Post.query.all()
    return render_template('profile.html',user=user,post=post,form=form)

@users.route('/edit/<string:username>',methods=['GET','POST'])
@login_required
def edit(username):
    form=EditForm()
    user=User.query.filter_by(username=current_user.username)
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.location=form.location.data
        current_user.about_me=form.about_me.data
        db.session.commit()
        return redirect(url_for('users.profile',username=current_user.username))
        flash('Your profile has been saved','info')
    elif request.method =='GET':
        form.username.data =current_user.username
        form.location.data=current_user.location
        form.about_me.data=current_user.about_me
    return render_template('edit.html',form=form,user=user)
