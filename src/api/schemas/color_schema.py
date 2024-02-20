# Class to serialize/deserialize data (json-python and python-json)
# Understand how the model works, what are the data the model works with

from api import ma
from ..models import color_model
from marshmallow import fields

class ColorSchema(ma.SQLAlchemySchema):
    # This class will describe the fields
    class Meta:
        #Define color model
        model = color_model.Color
        # Define which fields to return upon request to api
        # fields = ("id", "color", "value") # To return with id
        fields = ("color", "value")
    # The schema also validates the type of data
    color = fields.String(required=True)
    value = fields.String(required=True)
