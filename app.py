#!/usr/bin/env python

import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

def generate_numbers(st, end, cnt=126):
    _cnt = cnt
    _adds = []
    _r = list(range(st, end))
    while _cnt > 0:
        _adds += zip(random.sample(_r, len(_r)), random.sample(_r, len(_r)))
        _cnt = _cnt - len(_r)
    return _adds[:cnt]

@app.route('/singledigit')
def singledigit():
    return render_template("addition.html", title="Single digit additions", additions=generate_numbers(1, 10))

@app.route('/doubledigit')
def doubledigit():
    return render_template("addition.html", title="Double digit additions", additions=generate_numbers(10, 100))

if __name__ == '__main__':
    app.run(debug=True)
