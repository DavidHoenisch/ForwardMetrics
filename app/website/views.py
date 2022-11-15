from flask import Blueprint, render_template


views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template("home.html")

@views.route("/login")
@views.route("/signup")
def login():
    return render_template("discord.html")
