from flask import Blueprint, render_template

docs = Blueprint("docs", __name__)

@docs.route('/docs')
@docs.route('/docs_table')
def docs_table():
    return render_template("docs_table.html")

@docs.route("/upload_predictions")
def upload_predictions():
    return render_template("upload_predictions.html")


