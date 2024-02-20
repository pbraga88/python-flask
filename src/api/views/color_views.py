from flask import app
from flask.helpers import make_response
from flask.json import jsonify
from flask_restful import Resource
from api import api
from ..schemas import color_schema
from flask import request
from ..entities import color
from ..services import color_service

class ColorList(Resource): 
    def get(self):
        """
        List the whole list of colors
        ---
        responses:
          200:
            description: Colors listed
            schema:
              id: Color
              properties:
                color:
                  type: string
                value:
                  type: string
        """
        colors = color_service.list_colors()
        #many=True to deserialize more than one object
        cs = color_schema.ColorSchema(many=True)
        
        return make_response(cs.jsonify(colors), 200)

    def post(self):
        """
        Insert a new color
        ---
        parameters:
        - in: body
          name: color
          description: Create a new color
          schema:
            type: object
            required:
              - color
              - value
            properties:
              color:
                type: string
              value:
                type: string
        responses:
          201:
            description: Color successfully created
            schema:
              id: Color
              properties:
                color:
                  type: string
                value:
                  type: string
          400:
            description: Bad request
        """
        # create a instance of ColorSchema
        cs = color_schema.ColorSchema()
        # Validade the data in request body
        validate = cs.validate(request.json)
        if validate:
            # Generate json format error response. 400 = Bad Request
            return make_response(jsonify(validate), 400)
        else:
            # Capture request data
            color_retrieve = request.json["color"]
            value_retrieve = request.json["value"]
            color_new = color.Color(color=color_retrieve, value=value_retrieve)
            # Call method insert_value and give the above as input
            result = color_service.insert_color(color_new)
            # return and serialize the schema data
            # and transform python in json to return
            return make_response(cs.jsonify(result), 201) # 201 = Created

class ColorDetail(Resource):
    # Get by id
    def get(self, id):
        """
        List color based on given id
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: Colors listed
            schema:
              id: Color
              properties:
                color:
                  type: string
                value:
                  type: string
          404:
            description: Color not found
        """

        # First verify if 'color' exists
        color = color_service.list_color_id(id)
        if color is None: # if id does not exist
            return make_response(jsonify("Color not found"), 404)
        else:
            # Create the object which will translate into json
            # Note that the 'many' attribute is not used here since 
            # only one color is being returned
            cs = color_schema.ColorSchema()
            return make_response(cs.jsonify(color), 200)
 
    # Edit by id
    def put(self, id):
        """
        Edit color based on given id
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            name: Edit color
            description: Edit an existing color
            schema:
              type: object
              required:
                - color
                - value
              properties:
                color:
                  type: string
                value:
                  type: string
        responses:
          200:
            description: Color successfully edited
            schema:
              id: Color
              properties:
                color:
                  type: string
                value:
                  type: string
          404:
            description: Color not found
          400:
            description: Bad request
        """

        # First verify if 'color' exists
        color_bd = color_service.list_color_id(id)
        if color_bd is None: # if id does not exist
            return make_response(jsonify("Color not found"), 404)
        
        cs = color_schema.ColorSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # Capture request data
            colorRet = request.json["color"]
            valueRet = request.json["value"]
            color_new = color.Color(color=colorRet, value=valueRet)
            color_service.edit_color(color_bd, color_new)
            updated_color = color_service.list_color_id(id)
            return make_response(cs.jsonify(updated_color), 200)
    # Remove by id 
    def delete(self, id):
        """
        Remove color based on given ID
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          204:
            description: Color successfully removed
          404:
            description: Color not found
        """
        color = color_service.list_color_id(id)
        if color is None: # if id does not exist
            return make_response(jsonify("Color not found"), 404)
        color_service.remove_color(color)
        return make_response('', 204) # 204 = Request and deletion successfull

class ColorDetailByValue(Resource):
    # Get by value
    def get(self, color):
        """
        List color based on given color name
        ---
        parameters:
          - in: path
            name: color
            type: string
            required: true
        responses:
          200:
            description: Colors listed
            schema:
              id: Color
              properties:
                color:
                  type: string
                value:
                  type: string
          404:
            description: Color not found
        """

        # First verify if color value exists
        color_rgb = color_service.list_color_value(color)
        if color_rgb is None: # if color does not exist
            return make_response(jsonify("Color not found"), 404)
        else:
            # Create the object which will  translate into json
            # Note that the 'many' attribute is not used here since 
            # only one color is being returned
            cs = color_schema.ColorSchema()
            return make_response(cs.jsonify(color_rgb), 200)
   
    def delete(self, color):
        """
        Remove color based on given color name
        ---
        parameters:
          - in: path
            name: color
            type: string
            required: true
        responses:
          204:
            description: Color successfully removed
          404:
            description: Color not found
        """
        color_rgb = color_service.list_color_value(color)
        if color_rgb is None: # if id does not exist
            return make_response(jsonify("Color not found"), 404)
        color_service.remove_color(color_rgb)
        return make_response('', 204) # 204 = Request and deletion successfull

# Register classes as API resources. 
# Class name and API route shall be given
api.add_resource(ColorList, '/colors')
api.add_resource(ColorDetail, '/colors/<int:id>') # use <int:id> since the type to
                                                   # be retrieved is int
api.add_resource(ColorDetailByValue, '/colors/<string:color>')   