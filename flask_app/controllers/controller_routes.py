from flask_app import app
from flask import render_template, redirect, session, request, flash

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register')
def register():
  return render_template('register.html')

# DASHBOARD
@app.route("/dashboard")
def user_show():
  # if not 'user_id' in session:
  #   flash("Please log in to view this.")
    # return redirect('/')
  return render_template('dashboard.html')

# @app.errorhandler(404)
# def server_error(e):
#   print('Error Function')
#   return render_template('error.html')