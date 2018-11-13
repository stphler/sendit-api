
from flask import Flask
# we import created blueprints to register them
from .api.v1 import version1
from .test.v1 import TestDataParcel


def create_app():
    app = Flask(__name__)
    # we register the blueprint
    app.register_blueprint(version1)
    # register more blueprints in a similar manner
    return app
