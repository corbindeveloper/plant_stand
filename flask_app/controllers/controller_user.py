from curses import flash
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_user, model_plant
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

############################################################

# REGISTER
@app.route("/user/register", methods=["POST"])
def user_register():
  user = model_user.User.get_user_by_email(request.form)
  if not model_user.User.validate_new_user(request.form):
    return redirect('/register')
  else:
    data = {
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'email': request.form['email'],
      'password': bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)

   
    # proceed with login
    session['user_id'] =  model_user.User.create_new_user(data)
    session['user_email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']


    flash("Please Login!")
    return redirect('/profile/create')


############################################################


# LOGIN
@app.route("/user/login", methods=["POST"])
def login_user():
  # determine if the email  exist
  user = model_user.User.get_user_by_email(request.form)
  if not user:
    flash("Email does not exist")
    return redirect('/')
  # check the password 
  if not bcrypt.check_password_hash(user.password, request.form['password']):
    flash("Incorrect Password.")
    return redirect('/')
  # proceed with login
  session['user_id'] = user.id
  session['user_email'] = user.email
  session['first_name'] = user.first_name
  session['last_name'] = user.last_name

  return redirect('/dashboard')

############################################################


# LOGOUT
@app.route("/user/logout")
def logout():
  session.clear()
  flash("Logged out -- Please sign back in.")
  return redirect('/')


############################################################


# # DASHBOARD
# @app.route("/dashboard")
# def user_show():
#   if not 'user_id' in session:
#     flash("Please log in to view this.")
#     return redirect('/')
#   return render_template('dashboard.html')


############################################################

# RENDER CREATE PROFILE FORM
@app.route("/profile/create")
def profile_create_render():
  return render_template('profile_create.html')


############################################################

# CREATE PROFILE
@app.route("/profile/create/success", methods=["POST"])
def profile_create():

  # VALIDATE ENTRIES

  data = {
   'id': session['user_id'],
   'bio': request.form['bio'],
   'exp': request.form['exp'], 
   'state': request.form['state'],
   'wishlist': request.form['wishlist'],
  }
  print(data)
  user = model_user.User.profile_create(data)

  # proceed with login
  # if request.method == "POST":
  #   session['user_id'] = user.id
  #   session['user_email'] = user.email
  #   session['first_name'] = user.first_name
  return redirect('/dashboard')


############################################################

# VIEW PERSONAL PROFILE
@app.route("/profile/view")
def profile_show():
  user = model_user.User.get_user_by_id({'id': session['user_id']})
  # plant = model_plant.Plant.get_plant_by_id({'id': id})
  return render_template('profile_view.html', user=user)


############################################################

# EDIT PERSONAL PROFILE
@app.route("/profile/edit")
def profile_edit():
  user = model_user.User.get_user_by_id({'id': session['user_id']})
  return render_template('profile_edit.html', user=user)


############################################################

# UPDATE PERSONAL PROFILE
@app.route("/profile/<int:id>/update", methods=["POST"])
def profile_update(id):
  data = {
    **request.form,
    'id': id
  }

  model_user.User.update_user_profile(data)
  return redirect('/profile/view')


############################################################

# VIEW OTHERS PROFILE
@app.route("/profile/view/<int:id>")
def profile_show_user(id):
  user = model_user.User.get_user_by_id({ 'id': id })
  return render_template('profile_view_user.html', user=user)





