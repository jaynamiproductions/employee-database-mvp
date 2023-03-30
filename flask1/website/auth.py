from flask import Blueprint, render_template as rt, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
                login_user(user,remember=False)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='Error')
        else:
            flash('Email does not exist', category='Error')
    return rt('login.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address is already taken.',category='Error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='Error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='Error')
        elif password1 != password2:
            flash("Passwords don't match.", category='Error')
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="Error")
        else:
            newuser = User(email=email,firstname=firstname,password=generate_password_hash(password1,method='sha256'))
            db.session.add(newuser)
            db.session.commit()
            flash('Account sign up successful. Please log in.',category='Success')
            return redirect(url_for('auth.login'))
    return rt('sign_up.html',user=current_user)