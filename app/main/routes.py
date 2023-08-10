from app.main import bp
from flask import redirect, current_app

@bp.route("/")
def index():
    return "<h1> Hello Main Blueprint! </h1>"
