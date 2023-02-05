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

@app.route("/login_added_new_work", methods=["POST"])
def login_add():
    #costumer = request.form["costumer"]
    #work_type = request.form["work_type"]
    #price = request.form["price"]
    #status = request.form["status"]
    #start_date = request.form["start_date"]
    #TO DO
    user = session["username"]
    admin = database_methods.get_admin(user)
    return render_template("login.html", user=user, admin=admin)

@app.route("/search")
def search():

    return render_template("search.html")

@app.route("/add")
def add():

    return render_template("add.html")

@app.route("/info", methods=["POST"])
def info():
    intrest = request.form["intrest"]
    if intrest == "costumer":
        count = database_methods.get_count_by_costumer(session["username"])
    else:
        count = "No info"
    return render_template("info.html", intrest=intrest, count=count)