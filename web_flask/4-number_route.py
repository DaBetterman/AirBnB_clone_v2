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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def python(text):
    """Returns 'Python' + the argument value, if no arg value
        then it will return 'is cool' as a default value"""
    replacer = text.replace('_', ' ')
    return 'Python ' + replacer


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
