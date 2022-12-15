import os

from flask import Flask
from .extensions import db

from .blueprints.auth import auth
from .blueprints.api import api
from config import config as configs


def create_app(conf='default'):
    app = Flask(__name__)

    config_name = conf
    # init the config
    if not isinstance(conf, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(configs[config_name])

    # set up extensions
    db.init_app(app)

    # init database under app context
    # see: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(api)

    return app
