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

def generate_words():
    with open('wordlist1.txt', 'r') as fh:
        txt = fh.read()
    for word in txt.split():
        index = random.randint(0, len(word))
        word[index] = '_'
        print(word)
    return None

@app.route('/mul')
def mul():
    return render_template("addition.html", operator='x', title="Single digit multiplication", additions=generate_numbers(1, 10))

@app.route('/bigmul')
def bigmul():
    return render_template("addition.html", operator='x', title="Double digit multiplication", additions=generate_numbers(10, 100))

@app.route('/add')
def add():
    return render_template("addition.html", operator='+', title="Single digit additions", additions=generate_numbers(1, 10))

@app.route('/bigadd')
def bigadd():
    return render_template("addition.html", operator='+', title="Double digit additions", additions=generate_numbers(10, 100))

@app.route('/sub')
def sub():
    return render_template("addition.html", operator='-', title="Single digit subtractions",
                            additions=generate_numbers(1, 10, operator='-'))

@app.route('/bigsub')
def bigsub():
    return render_template("addition.html", operator='-', title="Double digit subtractions",
                            additions=generate_numbers(10, 100, operator='-'))

@app.route('/words')
def words():
    # return render_template("words.html", words=generate_words())
    generate_words()
    return "OK"

@app.route('/seq')
def seq():
    # return render_template("words.html", words=generate_words())
    return render_template("seq.html")
if __name__ == '__main__':
    app.run(debug=True)
