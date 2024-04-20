#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns 'C' + the argument content"""
    replacer = text.replace('_', ' ')
    return 'C ' + replacer

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
