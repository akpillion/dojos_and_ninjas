from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id' : dojo_id
    }
    dojo = Dojo.get_one(data)
    ninjas = Ninja.all_ninjas_dojo(data)
    return render_template('show_dojo.html', dojo = dojo, ninjas = ninjas)
