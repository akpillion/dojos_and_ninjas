from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.models_ninja import Ninja
from flask_app.models.models_dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL

# Create Ninja Page
@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/')