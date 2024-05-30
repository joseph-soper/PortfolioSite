''' My Portfolio App '''
from flask import Flask, render_template, Blueprint
from home import home

app = Flask(__name__)
app.register_blueprint(home, url_prefix="/")

home = Blueprint(__name__, "home")

@home.route("/")
def home_page():
    ''' return home page '''
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, port=8080)
