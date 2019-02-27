from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

from .forms import UserForm,UpdateProfile
from .. import db,photos


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form = UserForm()
    title = 'Home - Welcome to The best user Website Online'

    return render_template('new_user.html','comment.html',title = title, user_form=form)
    
    return render_template('comment.html',title = title, user_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pickup/')
def pickuplines():

    return render_template("index.html")


@main.route('/interview/')
def interview():

    return render_template("index.html")

@main.route('/product/')
def product():

    return render_template("index.html")

@main.route('/promotion/')
def promotion():

    return render_template("index.html")


@main.route('/newpitch/')
def newpitch():

    return render_template("index.html")

@main.route('/comment/')
def comment():

    return render_template("index.html")

@main.route('/vote/')
def vote():

    return render_template("index.html")

@main.route('/comment/')
def comment():

    return render_template("index.html")





