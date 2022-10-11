from gettext import Catalog
from hashlib import sha256
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first() 
        print(email, password) # Remove me
        if user:
            if check_password_hash(user.password, password):
                flash("Login Successful",'message')
                login_user(user, remember=True)
                return redirect(url_for("user_dash.dashboard"))
            else: 
                flash("Incorrect password",'error')
        else: 
            flash("User does not exist", 'error')
    return render_template("login2.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(fname, lname, email, password1) # Remove me
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("email already in use", "error")
            
        elif password1 != password2:
            flash('Passwords do not match', "error")
        elif len(password1) < 12:
            flash('Passwords must be a minimun of 12 character long', "error")
        else:
            new_user = User(email=email, fname=fname, lname=lname, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('User account created', "message")
            login_user(new_user, remember=True)
            return redirect(url_for('user_dash.dashboard'))
    return render_template("signup.html")

    ## Generate random account number that will be used to id users across db tables? 

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", category='success')
    return redirect(url_for("views.home")) 