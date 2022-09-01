#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def method_name():
    pass

@app.route('/login')
def method_name():
    pass

@app.route('/register')
def method_name():
    pass

@app.route('/dashboard')
def method_name():
    pass

