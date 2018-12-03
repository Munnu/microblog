from flask import render_template, flash, redirect, url_for

# import 'app' variable from the app package (this package)
from app import app

# import LoginForm from forms.py
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    # instantiate a LoginForm object
    form = LoginForm()

    # Call validate() only if the form is submitted.
    # This is a shortcut for form.is_submitted() and form.validate()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    # send the instantiated LoginForm object to the view (template)
    # form (lhs) is the jinja template var name (kwarg), form (rhs) is the variable above
    return render_template('login.html', title='Sign In', form=form)
