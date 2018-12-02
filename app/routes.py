from flask import render_template

# import 'app' variable from the app package (this package)
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # user(left hand side) is a kwarg, user (right hand side) is the variable above
    return render_template('index.html', title='Home', user=user, posts=posts)
