from app.main import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html", nav_type="about_me")


@bp.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template("projects.html", nav_type="projects")


@bp.route('/work_experience', methods=['GET', 'POST'])
def work_experience():
    return render_template("work_experience.html", nav_type="work_experience")