"""API route for the About page"""

import os
import openai
from flask_restx import Namespace, Resource

api = Namespace('about', description='About page operations')

openai.api_key = os.getenv("OPENAI_API_KEY")

class GenerateAbout(Resource):
    def get(self):
        response = openai.Completion.create(
            model="text-davinci-001",
            prompt="Tell me about universal basic income.",
            temperature=0.75,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

        return response

api.add_resource(GenerateAbout, "")