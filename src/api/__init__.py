from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger

app = Flask(__name__) # Create Flask application
app.config.from_object('config') # Get configurations from config.py
# Configure communication between the SQLAlchemy and the sql database
# Enable SQLAlchemy in the flask app
db = SQLAlchemy(app)
# Enable Marshmallow. After SQLAlchemy since it's linked to the database
ma = Marshmallow(app)
# Migrate will manage migration from app in mysql database
migrate = Migrate(app, db)

api = Api(app) # This api is created based upon flask_restful

swagger = Swagger(app)

from .views import color_views
from .models import color_model