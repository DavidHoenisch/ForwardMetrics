import string
import os
from secrets import choice
from re import A
from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from werkzeug.utils import secure_filename

db = SQLAlchemy()
UPLOAD_FOLDER = "/home/dhoenisch/Documents/forward-metrics-web-application/app/website/uploads"
DOWNLOAD_FOLDER = "/home/dhoenisch/Documents/forward-metrics-web-application/app/website/downloads"
ALLOWED_EXTENSIONS = {'csv','xcel'}
DB_NAME = "database.sql"
cookie_string = ''.join([choice(string.ascii_uppercase + string.digits) for i in range(124)])
def forwardmetrics():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = cookie_string
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    db.init_app(app)

    from .models import User

    from .views import views
    from .auth import auth
    from .user_dashboard import user_dash
    from .docs import docs
    from .api import api
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(user_dash, url_prefix="/user/" )
    app.register_blueprint(docs, url_prefix="/") 
    app.register_blueprint(api, url_prefix="/api/")


    check_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def check_db(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
