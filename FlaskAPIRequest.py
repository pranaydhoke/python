__author__      = "Pranay Dhoke"
__copyright__   = ""

from flask import Flask
from flask import request
from flask import Flask,flash, redirect, render_template, request, session, abort
import os

app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'] == 'Admin',request.form['password'] == 'password'):
                return log_the_user_in(request.form['username'])

        else:
            error ='Invalid username'
    else:
         return render_template('login.html')

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

def show_the_login_form():
    return "Successfully login"

def do_Login():
    return "login"

