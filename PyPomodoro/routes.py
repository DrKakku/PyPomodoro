import os

from flask import jsonify, render_template, request
from PyPomodoro import app


Phases = [{"name":"Standby","Colour":"Green"},
          {"name":"Work","Colour":"Orange"},
          {"name":"Rest","Colour":"Blue"},
          {"name":"Long Work","Colour":"Red"},
          ]

Init_State = {"Phase":Phases[3]}


@app.route('/')
@app.route('/home')
def home():

    return render_template('homepage.html', State = Init_State)

