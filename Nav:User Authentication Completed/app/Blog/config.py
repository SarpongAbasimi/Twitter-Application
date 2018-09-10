import os

class Config(object):
    SECRET_KEY=os.environ.get('NANA')
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    print(SQLALCHEMY_DATABASE_URI)
