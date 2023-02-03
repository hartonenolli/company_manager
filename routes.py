from app import app
from flask import render_template, request, redirect, session
import database_methods

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        user = session["username"]
    else:
        user = request.form["name"]
        session["username"] = user
    admin = database_methods.get_admin(user)
    return render_template("login.html", user=user, admin=admin)

@app.route("/search")
def search():

    return render_template("search.html")