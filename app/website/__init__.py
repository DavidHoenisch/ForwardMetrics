import string
from secrets import choice
from flask import Flask

cookie_string = ''.join([choice(string.ascii_uppercase + string.digits) for i in range(124)])


def forwardmetrics():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = cookie_string

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app
