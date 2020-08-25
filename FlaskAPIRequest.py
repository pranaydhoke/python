__author__      = "Pranay Dhoke"
__copyright__   = "Technospace"

from flask import request
from flask import Flask

app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_Login()
    else:
        return show_the_login_form()    

def show_the_login_form():
    return "Successfully login"

def do_Login():
    return "login"

