from flask import Flask

# Define instances of plugins here (SQLalchemy, etc)


def create_app():
    """
    Create_app() sets up a context for our flask app. It
    handles all of the configuration necessary. All plugins must
    be defined here otherwise flask will not see them
    """

    # Setup and configure our app from ../config.py
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Init the plugins here

    # This creates the current app context and returns it
    with app.app_context():

        # include our routes
        from . import routes

        # Register blueprints here

        return app