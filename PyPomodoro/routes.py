import os

from flask import jsonify, render_template, request
from PyPomodoro import app



@app.route('/')
@app.route('/home')
def home():

    return render_template('homepage.html', route=os.getcwd())

