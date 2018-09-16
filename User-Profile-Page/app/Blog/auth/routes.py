from flask import Blueprint,render_template,redirect,flash,url_for,request
from Blog.auth.forms import RegistrationForm,LoginForm
from Blog.models import User
from Blog import bcrypt,db,current_user
from flask_login import login_user,logout_user,login_required



auth=Blueprint('auth',__name__)


@auth.route('/register/',methods=['GET','POST'])
def register():
     form=RegistrationForm()
     if form.validate_on_submit():
         hash_password =bcrypt.generate_password_hash(form.password.data)
         user=User(name=form.name.data,username=form.username.data,email=form.email.data,password=hash_password)
         db.session.add(user)
         db.session.commit()
         return redirect(url_for('auth.login'))
     return render_template('register.html',form=form)


@auth.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get(next)
            return redirect(request.args.get(next_page)) if next_page else redirect(url_for('users.index'))
        else:
            flash('The email and password you entered did not match our records. Please double-check and try again.','danger')
    return render_template('login.html',form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
