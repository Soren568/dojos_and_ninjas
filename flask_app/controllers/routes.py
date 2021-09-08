from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo

# * ======================= HOME PAGE ==============================
@app.route('/')
def all_dojos():
    return render_template('index.html', dojos=Dojo.get_all())

@app.route('/create_dojo', methods=['POST'])
def dojo_create():
    Dojo.save(request.form)
    return redirect('/')

# Redirect to ninja creation
@app.route('/new_ninja')
def dojo_to_ninja():
    return render_template('new_ninja.html', dojos=Dojo.get_all())

# * ======================= NEW NINJA PAGE ==============================

@app.route('/create_ninja', methods=['POST'])
def ninja_create():
    Ninja.save(request.form)
    id = request.form['dojo_id']
    return redirect(f"/dojo_info/{id}") 

# * ======================= DOJO SHOW PAGE ==============================

@app.route('/dojo_info/<int:id>')
def dojo_info(id):
    data={
        "id":id
    }
    return render_template("dojo.html", dojo=Dojo.get_one(data))