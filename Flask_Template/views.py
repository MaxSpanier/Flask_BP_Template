from Flask_Template import app

@app.route("/")
def index():
    return "Hello World!"