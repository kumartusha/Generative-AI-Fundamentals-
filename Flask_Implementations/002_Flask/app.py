from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/services")
def sevices():
    print("Hello I'm the first")
    return render_template("services.html")


@app.route("/about")
def about():
    print("Hello I'm the first")
    return render_template("about.html")


@app.route("/contact")
def contact():
    print("Hello I'm the first")
    return render_template("contact.html")


@app.route("/")
def home():
    print("Hello I'm the first")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
