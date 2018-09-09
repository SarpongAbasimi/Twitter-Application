from flask import Blueprint,render_template


users=Blueprint('users',__name__)



@users.route('/')
def index():
    return render_template('index.html')

@users.route('/profile/')
def profile():
    return render_template('profile.html')
