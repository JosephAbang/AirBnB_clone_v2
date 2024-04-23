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


@app.route('/python/')
@app.route('/python/<text>')
def py_text(text='is cool'):
    """Display string python with concatenated text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_number(n=None):
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
