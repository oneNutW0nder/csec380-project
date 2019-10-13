"""
This file contains the database models that will be used
for our web application
"""

from . import db
from datetime import datetime
from bcrypt import gensalt, hashpw, checkpw
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    Defines the model for users
    """

    __tablename__ = "users"

    # Define each user entry into the database
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), index=True, unique=True, nullable=False)
    cookie = db.Column(db.String(255))
    cookie_expiration = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    def __init__(self, username, password):
        """
        Setup the class vars and initialize a user

        :param username: The name of the user
        :param password: The password for the user
        """

        self.username = username
        User.set_password(self, password)

    def set_password(self, password):
        """
        Sets a user's password by hashing and salting the provided password

        :param password: The password for the given user
        """

        try:
            password = bytes(password, "utf-8")
            self.password = hashpw(password, gensalt())
        except TypeError:
            pass

    def check_password(self, password):
        """
        Check a user's password. Will be used for login

        :param password: The password entered by a user
        :return: True or false for password match or fail
        """

        return checkpw(bytes(password, "utf-8"), bytes(self.password, "utf-8"))

    def get_id(self):
        """
        Return the id of a given user
        """

        return self.id

    def check_valid_cookie(self, session_cookie):
        """
        Used to make sure a user's session is still valid

        :param session_cookie: The current session cookie for a user
        :return: True or false based on whether or not a user's 
        session is vlaid
        """

        # Check if passed cookie is user's cookie
        if self.cookie == session_cookie:
            # Check if cookie is still valid
            if self.cookie_expiration > datetime.now():
                return True
        else:
            return False

    def is_authenticated(self, session_cookie):
        """
        Check if the given user is authenticated

        :param session_cookie: The given user's session cookie
        :return: True or false based on if the user has been authenticated
        """

        if self.cookie_expiration > datetime.now():
            return True
        else:
            return False

    def is_anonymouse(self):
        """
        This is a function that is required to be implemented to use
        Flask-Login. An actual user will return false because they are
        obviously not anonymous.
        """

        return False
