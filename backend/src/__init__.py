from flask import Flask

def create_app(script_info=None):

    app = Flask(__name__)
    app.config.from_object("src.config.DevelopmentConfig")

    #import API Blueprint object created in api/__init__.py
    from src.api import api_bp

    #Register the blueprint to the Flask object (app) with a url route
    app.register_blueprint(api_bp, url_prefix="/api")

    #Set flask host to be open and set port to 8080
    app.run(host="0.0.0.0", port=8080)

    return app