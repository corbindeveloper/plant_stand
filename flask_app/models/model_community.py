from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Community:
  def __init__( self , data ):
    self.id = data['id']
    self.name = data['name']
  
##########################################################

  # GENERAL GET ALL FROM  COMMUNITIES 
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM communities;"
    results = connectToMySQL(DATABASE).query_db(query)
    if results:
      all_communities = []
      for dict in results:
        all_communities.append( cls(dict) )
      return all_communities
    return []


##########################################################

  # GENERAL GET ALL from COMMUNITIES 



##########################################################

  # GENERAL GET ALL from COMMUNITIES 




##########################################################

  # GENERAL GET ALL from COMMUNITIES 