#!/usr/bin/python3

"""
    Script starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """display 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display string 'hbnb'"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display text concatenation"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>')
def py_text(text):
    """Display string python with concatenated text"""
    if len(text) == 0:
        text = "is cool"
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
