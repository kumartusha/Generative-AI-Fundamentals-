from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#  Create the Database connection for the flask application with the help of the SQLAlchemy which is called the Python ORM
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


#  URL Rendering Methods..*************************************************
@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        # below title and desc have the input value
        title = request.form["title"]
        desc = request.form["desc"]

        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        else:
            #  Show the pop up here
            # return render_template("alert.html")
            print("Enter Some text")

    alltodo = Todo.query.all()
    return render_template("index.html", alltodo=alltodo)


@app.route("/show")
def show():
    alltodo = Todo.query.all()
    print(alltodo)
    # return render_template("index.html")
    return "This is the show page"


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]

        if title and desc:
            todo = Todo.query.filter_by(sno=sno).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect("/")
        else:
            #  Show the pop up here
            # return render_template("alert.html")
            print("Enter Some text")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
