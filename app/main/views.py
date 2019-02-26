from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie
# from .forms import UserForm
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

    return render_template('new_user.html',title = title, user_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)





