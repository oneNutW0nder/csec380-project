"""
This file defines the routes that will be served by our Flask app
The "current_app" value references the current application context
that was created in __init__.py
"""

from flask import render_template, current_app, request, redirect
from . import loginmanager, db
from application.models import User


@loginmanager.user_loader
def load_user():
    """
    Loads the user context for use in session management
    """

    return User.query.get(int(id))


@current_app.route("/hello", methods=["GET"])
def hello():
    """
    This route is for a hello world test
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
        else:
            # Failure of passwords matching
            return render_template("registererror.html")
