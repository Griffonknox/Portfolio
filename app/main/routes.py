from app.main import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")


