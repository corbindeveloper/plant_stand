from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_community
from flask_app.models import model_user


# RENDER CREATE COMMUNITY FORM
@app.route("/community/create")
def community_create():
  # VALIDATE USER IS LOGGED IN

  return render_template('community_create.html')

############################################################

# SUBMIT CREATE COMMUNITY 
@app.route("/community/create/success")
def community_create_success():
  return render_template('community_create.html')

############################################################

# VIEW ALL COMMUNITIES
@app.route("/community/view/all")
def community_get_all():
  # VALIDATE USER IS LOGGED IN

  all_communities = model_community.Community.get_all()
  return render_template('community_view_all.html', all_communities=all_communities)

############################################################

# VIEW SPECIFIC COMMUNITY
@app.route("/community/view/<int:id>")
def community_view_id(id):
  return render_template('community_view.html')

############################################################

# VIEW 
@app.route("/community/view")
def community_view():
  return render_template('community_view.html')

############################################################

# Currently no plans to allow to change a community name,
# this protects against anyone changing the name to make 
# someone feel like they joined a group the didn't

############################################################
# DELETE
@app.route("/community/<int:id>/delete")
def community_delete(id):
  return redirect('/')