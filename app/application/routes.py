"""
This file defines the routes that will be served by our Flask app
The "current_app" value references the current application context
that was created in __init__.py
"""

from flask import render_template, current_app, request, redirect
from . import loginmanager, db
from application.models import User
from datetime import datetime, timedelta
from secrets import token_urlsafe


@loginmanager.user_loader
def load_user():
    """
    Loads the user context for use in session management
    """

    return User.query.get(int(id))


@current_app.route("/hello", methods=["GET"])
def hello():
    """ This route is for a hello world test
    """
    return render_template("hello.html")


@current_app.route("/", methods=["GET"])
def root():
    # Check if the user is logged in with valid session
    # if not logged in redirect to /login
    if request.method == "GET":
        return render_template("index.html")


@current_app.route("/login", methods=["GET", "POST"])
def login():
    # First check for method type
    # If GET --> check for valid session and redirect to homepage "/"
    # If POST --> grab user entered data and check database for existing user
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        return username, password


@current_app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpassword = request.form["confirmpassword"]

        if password == confirmpassword:
            # Continue registering
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
        else:
            # Failure of passwords matching
            return render_template("registererror.html")


def auth_user_session():
    """
    Makes sure a user is authenticated. Will be used to verify auth
    to access certain resources

    :return: Returns the user object if they are auth'd
    """
    if "user" in request.cookies:
        userid = request.cookie["user"]
        if userid:
            user = User.query.filter(User.id == userid).first()
            if user:
                if "session_cookie" in request.cookies and user.cookie == request.cookies["session_cookie"]:
                    if user.cookie_expiration > datetime.now():
                        return user

    # Return none if failure
    return None


def kill_session(user):
    """
    This kills a user's session by removing the cookie and updating the
    expiration to the current time. Used for logging out

    :param user: The user whose session to kill
    """

    # Destroy cookie
    user.cookie = None
    user.cookie_expiration = datetime.now()

    # Commit
    db.session.add(user)
    db.session.commit()


def update_session(user):
    """
    Used to update a user's session at login

    :param user: The user whose session to update
    """

    # Setup/update cookie
    user.cookie = token_urlsafe(64)
    user.cookie_expiration = datetime.now() + timedelta(hours=2)

    # Commit
    db.session.add(user)
    db.session.commit()
