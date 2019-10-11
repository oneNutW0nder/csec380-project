from flask import Flask

# Define instances of plugins here (SQLalchemy, etc)


def create_app():

    # Setup and configure our app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Init the plugins here

    with app.app_context():

        # include our routes
        from . import routes

        # Register blueprints here

        return app