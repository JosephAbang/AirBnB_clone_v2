#!/usr/bin/python3

"""
    Script starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def temp_num(n):
    """Retrieve template request by rendering"""
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def temp_even_odd(n):
    """Retrieve template request by rendering"""
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
