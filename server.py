from flask_app import app
from flask_app.controllers import controller_routes, controller_user, controller_community, controller_plant

# THE END
if __name__=="__main__":
   app.run(debug=True)