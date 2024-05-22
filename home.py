''' home page '''
from flask import Blueprint, render_template

home = Blueprint(__name__, "home")

@home.route("/")
def home_page():
    ''' return home page '''
    return render_template("index.html")
