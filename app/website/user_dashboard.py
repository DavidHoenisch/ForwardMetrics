from crypt import methods
from curses import erasechar, flash
from shutil import register_unpack_format
from urllib.parse import uses_relative
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from flask import request, flash, redirect, send_file, jsonify
from .proph import api_predict, EXPORT_FILE
from .proph import upload_predict
from . import db, allowed_file, UPLOAD_FOLDER, DOWNLOAD_FOLDER
from .models import Prefences
from werkzeug.utils import secure_filename
import os


user_dash = Blueprint("user_dash", __name__)

@user_dash.route("/userpanel")
@login_required
def dashboard():
    return render_template ("user_dashboard.html")

@user_dash.route("/prophet", methods=["GET", "POST"])
@login_required
def prophet():
    if request.method == 'POST':
        print("first check")
        if 'file' not in request.files:
            print('No file uploaded')
            return redirect(request.url)
        file = request.files['file']
        periods = request.form.get('periods')

        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_predict(file, int(periods))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            print("File uploaded")


    return render_template("prophet.html")
        
@user_dash.route("json_data")
def json_data():
    return ("test")


@user_dash.route("/download_page")
@login_required
def download_page():
    return render_template("downloads_page.html")

@user_dash.route("/downloads")
@login_required
def downloads ():
    path = os.path.join(DOWNLOAD_FOLDER, EXPORT_FILE)
    return send_file(path, as_attachment=True)



#    if request.method == "POST":
#        cfile = request.form.get('cfile')
#        if cfile == None:
#            print('no file select')
#        upload_predict(cfile)

#    if request.method == "POST":
#        ticker_symbol = request.form.get('ticker_symbol')
#        frequency = request.form.get('frequency')
#        api_key = "HEU9KOVRP7YN6H92" # Nuke me, for dev only
#        print(ticker_symbol, frequency) #

#        output = api_predict(ticker_symbol=ticker_symbol, api_key=api_key, frequency=frequency)
#        flash(output, 'message')
    return render_template("prophet.html")

@user_dash.route("/charts")
@login_required
def charts():
    return render_template("charts.html")

@user_dash.route("/alerts")
@login_required
def alerts():
    return render_template("alerts.html")

@user_dash.route("/preferences", methods=["POST", "GET"])
@login_required
def preferences():

    if request.method == "POST":
        av_api = request.form.get("av_key")
        user_id = current_user.id
        api_key = Prefences(user_id=user_id, av_api=av_api)
        db.session.add(api_key)
        db.session.commit()

        test_key = Prefences.query.filter_by(user_id=user_id).first()
        print(test_key)
        print(user_id)

    return render_template("preferences.html")

@user_dash.route("/json/<uuid>", methods=['GET'])
@login_required
def get_json(uuid):
    content = request.json
    print(content[''])
    return jsonify({"uuid":uuid})