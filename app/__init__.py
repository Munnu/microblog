from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
# specifies the view function that handles logins
login.login_view = 'login'

# imported at the bottom to prevent circular import
# between routes.py and this file
from app import routes, models
