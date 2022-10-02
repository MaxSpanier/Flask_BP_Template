from flaskr import app
from flask import render_template, url_for, flash, request

@app.route("/")
def index():
    flash("Success", "success")
    flash("Error", "error")
    return "Hello World!"
