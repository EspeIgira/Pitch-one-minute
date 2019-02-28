from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User,Pitches

from .forms import UserForm,UpdateProfile,AddPitch
from .. import db,photos


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # form = UserForm()

    

    title = 'Home - Welcome to The best user Website Online'
    all_pitches = Pitches.get_pitches()

    return render_template('new_user.html',title = title, all_pitches=all_pitches)

#Link user file and index file.............   

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

#Able to comment,vote.................
@main.route('/newpitch/',methods = ['GET','POST'])
@login_required
def newpitch():

    form = AddPitch()
  
    if form.validate_on_submit():
       
        description= form.description.data

        # Updated review instance
        new_pitch = Pitches(description = description ,user_id=current_user.id)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

   
    return render_template('addpitch.html',new_pitch=form)

@main.route('/comment/')
def comment():

    return render_template("comment.html")

@main.route('/vote/')
def vote():

    return render_template("index.html")







