from flask import Flask

app = Flask(__name__)

# imported at the bottom to prevent circular import
# between routes.py and this file
from app import routes
