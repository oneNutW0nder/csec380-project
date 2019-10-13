from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Define instances of plugins here (SQLalchemy, etc)
db = SQLAlchemy()
loginmanager = LoginManager()


def create_app():
    """
    Create_app() sets up a context for our flask app. It
    handles all of the configuration necessary. All plugins must
    be defined here otherwise flask will not see them
    """

    # Setup and configure our app from ../config.py
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    loginmanager.init_app(app)
    app.config.from_object("config.Config")

    # This creates the current app context and returns it
    with app.app_context():

        # include our routes
        from . import routes

        # Create tables from models
        db.create_all()
        db.session.commit()

        return app