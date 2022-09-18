from flaskr import app
from flask import render_template, url_for, flash, request

@app.route("/")
def index():
    flash("Hello", "success")
    return "Hello World!"
