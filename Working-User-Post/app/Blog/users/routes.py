from flask import Blueprint,render_template
from flask_login import login_required
from Blog.users.forms import Postform


users=Blueprint('users',__name__)


@users.route('/home')
@login_required
def index():
    form=Postform()
    return render_template('index.html',form=form)

@users.route('/profile/')
def profile():
    return render_template('profile.html')

@users.route('/hmm')
def che():
    return render_template('easy.html')
