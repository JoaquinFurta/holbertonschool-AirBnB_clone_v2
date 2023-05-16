#!/usr/bin/python3
"""
starting app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
      root page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
      hbnb route page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
      c route page
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """
      python route page
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
      n route page
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
      renders a template
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
