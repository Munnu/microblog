# import 'app' variable from the app package (this package)
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
