from flask import render_template, current_app

@current_app.route("/hello.html")
def hello():
    return render_template("hello.html")

@current_app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    current_app.run(debug=True)
