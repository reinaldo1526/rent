from flask import Flask
from config import Config

# Importing Flask-login
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login redirect config
login = LoginManager(app)
login.login_view = 'login' # this specifies what page to load for non-authorized users


from decemberblog import routes,models