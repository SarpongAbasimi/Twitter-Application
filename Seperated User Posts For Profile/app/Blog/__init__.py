from flask import Flask,url_for,render_template
from Blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_login import LoginManager,current_user
from flask_moment import Moment
import os

app=Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command('db',MigrateCommand)

moment=Moment(app)



bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='auth.login'
login_manager.login_message_category='info'

from Blog.users.routes import users
from Blog.auth.routes import auth
from Blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(auth)
app.register_blueprint(main)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
