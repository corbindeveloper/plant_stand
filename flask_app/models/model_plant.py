from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Plant:
  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
    self.sunlight = data['sunlight']
    self.water = data['water']
    self.owner_length = data['owner_length']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']
    self.user = None

  
  # Now we use class methods to query our database
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM plants;"
    
    results = connectToMySQL(DATABASE).query_db(query)
    
    if results:
      all_plants = []
      for plant in results:
        plants.append( cls(plant) )
      return plants
    return []


  # CREATE/ADD PLANT
  @classmethod
  def add_plant(cls, data):
    query = "INSERT INTO plants (name, sunlight, water, owner_length, user_id) VALUES (%(name)s, %(sunlight)s, %(water)s, %(owner_length)s, %(user_id)s)"
    return connectToMySQL(DATABASE).query_db(query, data)


  # GET SINGLE PLANT
  @classmethod
  def get_plant_by_id(cls, data):
    query = "SELECT * FROM plants JOIN users ON plants.user_id = users.id WHERE plants.id = %(id)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)
    item = results[0]
    plant = Plant(item)
    user_data = {
      "id": item["users.id"],
      "name": item["name"],
      "sunlight": item["sunlight"],
      "water": item["water"],
      "owner_length": item["owner_length"],
      "first_name": item["first_name"],
      "last_name": item["last_name"],
    }

    plant.user = User(user_date)

    return plant






