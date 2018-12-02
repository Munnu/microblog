from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# imported at the bottom to prevent circular import
# between routes.py and this file
from app import routes
