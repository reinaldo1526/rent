import os
basedir = os.path.abspath(os.path.dirname(__file__))
# Tell python to look at all files the same on any os (windows/mac,linux)

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False