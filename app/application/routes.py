"""
This file defines the routes that will be served by our Flask app
The "current_app" value references the current application context
that was created in __init__.py
"""


from flask import render_template, current_app


@current_app.route("/hello.html")
def hello():
    return render_template("hello.html")


@current_app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    current_app.run(debug=True)
