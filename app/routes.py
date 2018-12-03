from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse

# import 'app' variable from the app package (this package)
from app import app, db
from app.forms import RegistrationForm

# import LoginForm from forms.py
from app.forms import LoginForm

# flask login stuff
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
      
    # instantiate a LoginForm object
    form = LoginForm()

    # Call validate() only if the form is submitted.
    # This is a shortcut for form.is_submitted() and form.validate()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # get the arg called 'next' in the url
        # and whatever it's set to. next_page will be a dict, k, v of
        # {'next': <url or relative page path>}
        next_page = request.args.get('next')

        # if the login url does not have the 'next' argument
        # or url set to a relative path is null 
        # return to index; netloc is a security measure
        # to ensure that the url is within our current domain
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    # send the instantiated LoginForm object to the view (template)
    # form (lhs) is the jinja template var name (kwarg), form (rhs) is the variable above
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
