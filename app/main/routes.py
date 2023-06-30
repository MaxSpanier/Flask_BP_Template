from app.main import bp

@bp.route("/")
def index():
    return "<h1> Hello Main Blueprint! </h1>"