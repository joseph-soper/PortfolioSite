''' My Portfolio App '''
from flask import Flask
from home import home

app = Flask(__name__)
app.register_blueprint(home, url_prefix="/home")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
