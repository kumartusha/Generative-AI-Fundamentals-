from flask import Flask, render_template, request, redirect
import mysql.connector
import streamlit as st

#  we need to create the react app.

app = Flask(__name__)


def database_connect():
    return mysql.connector.connect(
        host="localhost", database="tushardb", password="1234!@#$Tushar", user="root"
    )


@app.route("/", methods=["GET", "POST"])
def main_func():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")
        address = request.form.get("address")
        password = request.form.get("feedback")

        #  here we have the data we need to save into the database

        database_conn = database_connect()
        cursor = database_conn.cursor()

        # Here we need to execute the query
        cursor.execute(
            cursor.execute(
                "INSERT INTO feedback (name, age, email, address, password) VALUES (%s, %s, %s, %s, %s)",
                (name, age, email, address, password),
            )
        )
        database_conn.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
