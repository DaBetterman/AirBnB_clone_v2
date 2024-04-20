#!/usr/bin/python3
# A script that starts a Flask web application

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    replacer = text.replace('_', ' ')
    return 'C ' + replacer

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text':'is cool'}, strict_slashes=False)
def python(text):
    replacer = text.replace('_', ' ')
    return 'Python ' + replacer

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
        return f'{n} is a number'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)