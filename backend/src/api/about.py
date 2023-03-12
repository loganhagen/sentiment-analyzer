"""API route for the About page"""

from flask_restx import Namespace, Resource

api = Namespace('about', description='About page operations')

class GenerateAbout(Resource):
    def get(self):
        return {"message": "universal basic income"}

api.add_resource(GenerateAbout, "")