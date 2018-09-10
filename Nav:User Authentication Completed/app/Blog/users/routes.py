from flask import Blueprint,render_template
from flask_login import login_required


users=Blueprint('users',__name__)


@users.route('/home')
@login_required
def index():
    return render_template('index.html')

@users.route('/profile/')
def profile():
    return render_template('profile.html')
