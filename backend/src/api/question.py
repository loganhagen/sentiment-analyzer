"""API route for the About page"""

import os
import openai
import flask
from flask import request
from flask_restx import Namespace, Resource

api = Namespace('question', description='Question page operations')

openai.api_key = os.getenv("OPENAI_API_KEY")

class AskQuestion(Resource):
    def get(self):
        # content = request.json

        # response = openai.Completion.create(
        #     model="text-davinci-001",
        #     prompt=content["input"],
        #     temperature=0.75,
        #     max_tokens=256,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0
        #     )

        # return response

        args = request.args

        return args
    
    def post(self):
        content = request.json

        response = openai.Completion.create(
            model="text-davinci-001",
            prompt=content["input"],
            temperature=0.75,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

        return response

api.add_resource(AskQuestion, "")