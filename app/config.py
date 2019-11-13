"""
This is the Flask Config class. It sets configuration settings for
our current app context defined in ./application/__init__.py
"""
import os


class Config:

    # TODO: Clean this up for final
    TESTING = True
    DEBUG = True
    SECRET_KEY = "dev"
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
