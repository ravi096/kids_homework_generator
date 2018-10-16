#!/usr/bin/env python

import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

def generate_numbers(st, end, operator='+', cnt=126):
    _cnt = cnt
    _adds = []
    _r = list(range(st, end))
    while len(_adds) < cnt:
        for ii in zip(random.sample(_r, len(_r)), random.sample(_r, len(_r))):
            if operator == '-':
                if ii[0] <= ii[1]:
                    continue
            _adds.append(ii)
        # _adds += zip(random.sample(_r, len(_r)), random.sample(_r, len(_r)))
        # _cnt = _cnt - len(_r)
    return _adds[:cnt]

@app.route('/singledigitaddition')
def singledigitaddition():
    return render_template("addition.html", operator='+', title="Single digit additions", additions=generate_numbers(1, 10))

@app.route('/doubledigitaddition')
def doubledigitaddition():
    return render_template("addition.html", operator='+', title="Double digit additions", additions=generate_numbers(10, 100))

@app.route('/singledigitsubtraction')
def singledigitsubtraction():
    return render_template("addition.html", operator='-', title="Single digit subtractions", 
                            additions=generate_numbers(1, 10, operator='-'))

@app.route('/doubledigitsubtraction')
def doubledigitsubtraction():
    return render_template("addition.html", operator='-', title="Double digit subtractions", 
                            additions=generate_numbers(10, 100, operator='-'))

if __name__ == '__main__':
    app.run(debug=True)
