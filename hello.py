from flask import Flask
import random
 # set FLASK_APP=hello.py
 # $env:FLASK_APP = "hello.py"
 # flask run

app = Flask(__name__)
print(__name__)
print(random.__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
