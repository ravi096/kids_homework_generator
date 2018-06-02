#!/usr/bin/env python

import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

def _get_simple_additions(cnt):
    # Returns 9 entries
    _r = list(range(1, 10))
    n = (cnt + 8) / 9
    _adds = []
    for _i in range(n):
        _adds = _adds + zip(random.sample(_r, 9), random.sample(_r, 9)) 
    return _adds

@app.route('/math')
def add():
    return render_template("addition.html", additions=_get_simple_additions(100))

if __name__ == '__main__':
    app.run(debug=True)
