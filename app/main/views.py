from flask import render_template,request,redirect,url_for
from . import main

# Views
@main.route('/')
@main.route('/home')

def home():
    name = "Time to get started "
    # context ={
    #     name: name
    # }
    return render_template('home.html', name=name)