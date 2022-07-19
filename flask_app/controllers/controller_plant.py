from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_plant
# from flask_app.controllers import controller_user

############################################################

# VIEW PERSONAL PLANT STAND
@app.route("/plantstand/view")
def stand_view():
  return render_template('plantstand_view.html')


############################################################

# RENDER NEW PLANT FORM
@app.route("/plantstand/new")
def stand_new():
  return render_template('plantstand_create.html')


############################################################

# ADD A PLANT
@app.route("/plantstand/add", methods=["POST"])
def plantstand_add():
  # VALIDATIONS 
  # HERE

  data = {
    'name': request.form['name'],
    'sunlight': request.form['sunlight'],
    'water': request.form['water'],
    'owner_length': request.form['owner_length'],
    # 'created_at': request.form['created_at'],
    'user_id': session['user_id']
  }

  print(data)
  model_plant.Plant.add_plant(data)
  return redirect('/dashboard')


############################################################

# EDIT PLANT 
@app.route("/plantstand/<int:id>/edit")
def plantstand_edit(id):
  return render_template('plantstand_edit.html')


############################################################

# UPDATE PLANT
@app.route("/plantstand/<int:id>/update", methods=["POST"])
def plantstand_update(id):
  return redirect('/')


############################################################

# VIEW OTHERS PLANT STANDS
@app.route("/plantstand/view/<int:id>")
def plantstand_show_user(id):
  return render_template('plantstand_view_user.html')