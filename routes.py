from app import app
from flask import render_template, request
import database_methods

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form["name"]
    admin = database_methods.get_admin(user)
    return render_template("login.html", user=user, admin=admin)