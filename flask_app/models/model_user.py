from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_user
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
   def __init__( self , data ):
      self.id = data['id']
      self.first_name = data['first_name']
      self.last_name = data['last_name']
      self.email = data['email']
      self.password = data['password']
      self.exp = data['exp']
      self.state = data['state']
      self.wishlist = data['wishlist']
      self.bio = data['bio']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   #######################################################

   # CREATE NEW USER ACCOUNT
   @classmethod
   def create_new_user(cls, data):
      query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
      result = connectToMySQL(DATABASE).query_db(query, data)
      return result

   #######################################################

   # GET USER BY EMAIL
   @classmethod
   def get_user_by_email(cls, data):
      query = "SELECT * FROM users WHERE email = %(email)s;"
      results = connectToMySQL(DATABASE).query_db(query, data)

      if len(results) == 0:
         return False
      else:
         return User(results[0])


   #######################################################

   # CREATE USER PROFILE
   @classmethod
   def profile_create(cls, data):
      query = "UPDATE users SET bio=%(bio)s, exp=%(exp)s, state=%(state)s, wishlist=%(wishlist)s WHERE id = %(id)s;"
      results = connectToMySQL(DATABASE).query_db(query, data)
      return results


   #######################################################

   # GET PERSONAL ID
   @classmethod
   def get_user_by_id(cls, data):
      query = "SELECT * FROM users WHERE id = %(id)s;"
      results = connectToMySQL(DATABASE).query_db(query, data)[0]
      print(results)
      return results


   #######################################################

   # UPDATE PROFILE
   @classmethod
   def update_user_profile(cls, data):
      query = "UPDATE users SET bio=%(bio)s, exp=%(exp)s, state=%(state)s, wishlist=%(wishlist)s WHERE id = %(id)s;"
      return connectToMySQL(DATABASE).query_db(query, data)

   #######################################################

   # STATIC METHODS
   # REGISTER|LOGIN VALIDATIONS
   @staticmethod
   def validate_new_user(data):
      is_valid = True

      if User.get_user_by_email(data):
         is_valid = False
         flash("Email seems to be already in use!")

      if len(data['first_name']) < 2:
         is_valid = False
         flash("First name should be atleast 2 characters!")

      if not EMAIL_REGEX.match(data['email']):
         is_valid = False
         flash("Email address is not formatted correct.")

      if len(data['password']) < 8:
         is_valid = False
         flash("Password must be at least 8 characters long.")
      
      if not data['password'] == data ['confirm_password']:
         is_valid = False
         flash("Passwords do not match.")
      
      return is_valid