"""
This file defines the routes that will be served by our Flask app
The "current_app" value references the current application context
that was created in __init__.py
"""
import os

from flask import render_template, current_app, request, redirect, make_response, flash
from . import loginmanager, db
from application.models import User
from application.models import Video
from datetime import datetime, timedelta
from secrets import token_urlsafe
from werkzeug.utils import secure_filename

# Setup vars for video uploads
EXTENSIONS = {"mp4", "flv"}
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOADS = os.path.join(BASE_DIR, "static", "uploads")
current_app.config["UPLOAD_FOLDER"] = UPLOADS


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
        user = auth_user_session()
        if user:
            return render_template("index.html")
        else:
            return redirect("/login")


@current_app.route("/login", methods=["GET", "POST"])
def login():
    """
    Hanldes the logic of loggin a user in. If the method is GET the
    user will have their session check and forwarded to the homepage
    if they have a valid session, otherwise they will be displayed the
    login page. If the method is POST the user's information will be
    validated and then logged in if the requirements are met.
    """

    if request.method == "GET":
        # Check if the user is auth'd
        user = auth_user_session()
        if user:
            # Send to homepage if they are auth'd
            return redirect("/")
        else:
            # Otherwise send back to login
            return render_template("login.html")

    if request.method == "POST":
        # Get values submitted through POST
        username = request.form["username"]
        password = request.form["password"]

        # Find the user in the database
        user = User.query.filter(User.username == username).first()
        if user:
            if user.check_password(password):
                # Update their cookie and commit
                cookie = update_session(user)
                db.session.add(user)
                db.session.commit()

                # Send cookie back in response
                response = make_response(redirect("/"))
                response.set_cookie("session_cookie", cookie)
                response.set_cookie("user", f"{user.id}")

                # Return
                return response
        return render_template("loginfailure.html")


@current_app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    Handles the logic for uploading vidoes. GET methods will just
    return the 'upload.html' template for the user if they are auth'd.
    POST methods will take the informaiton (video) and eitehr download it
    if a linke was provided or save it if the file was provided.
    """

    if request.method == "GET":
        # Check to see the user is auth'd
        user = auth_user_session()
        if user:
            # Render the upload template
            return render_template("upload.html")
        else:
            # User is not auth'd yet, have them login
            return redirect("/login")

    elif request.method == "POST":
        # handle upload logic
        user = auth_user_session()

        if user is not None:
            # Check for a file
            if "file" not in request.files:
                flash("No file found")
                return render_template("uploaderror.html")

            # File is in the request
            file = request.files["file"]

            if file.filename == "":
                # No filename
                flash("Invalid filename")
                return render_template("uploaderror.html")

            if file and allowed_filetype(file.filename):
                # Parse/generate filenames
                filename = secure_filename(file.filename)
                title = filename.rsplit(".", 1)[0]
                unique = unique_filename(filename)

                # Save the file locally
                file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], unique_filename))

                # Make a video object
                vid_obj = Video(user, title, unique)

                # Add and commit the new video object to the db
                db.session.add(vid_obj)
                db.session.commit()

                # Success!
                flash("File upload successful!")
                return redirect("/")

    # If everything else fails send them to login
    return redirect("/login")


@current_app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles the registration of a new user. A GET request will
    serve the html that includes the form for registration.
    A POST request with the proper parameters will
    register the user and add their info to the database.
    """

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmpassword = request.form["confirmpassword"]

        if password == confirmpassword:
            # Continue registering
            # TODO: ADD CHECK FOR EXISTING USER
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return render_template("registersuccess.html")
        else:
            # Failure of passwords matching
            return render_template("registererror.html")


@current_app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        user = auth_user_session()
        if user:
            return render_template("logout.html")
    if request.method == "POST":
        user = auth_user_session()
        if user:
            kill_session(user)
        return redirect("/login")


def auth_user_session():
    """
    Makes sure a user is authenticated. Will be used to verify auth
    to access certain resources

    :return: Returns the user object if they are auth'd
    """
    if "user" in request.cookies:
        userid = request.cookies["user"]
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
    :return: Returns the cookie that was created
    """

    # Setup/update cookie
    user.cookie = token_urlsafe(64)
    user.cookie_expiration = datetime.now() + timedelta(hours=2)

    # Commit
    db.session.add(user)
    db.session.commit()

    cookie = user.cookie
    return cookie


def allowed_filetype(filename):
    """
    Checks filetype by extension on the filename

    :param filename: Filename with extension
    :return: True if extension is supported; false if not
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS


def unique_filename(filename):
    """
    Creates a unique filename using the given filename and the current date

    :param filename: The string filename to make unique
    :return: returns a unique filename
    """

    filename_array = '.' in filename and filename.rsplit('.', 1)
    time = str(datetime.now().timestamp()).rsplit('.', 1)[0]
    return filename_array[0] + '-' + time + '.' + filename_array[1]