from app import app
from flask import render_template, request, redirect, session
import database_methods
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    username = request.form["name"]
    user_exists = database_methods.get_user(username)
    if user_exists:
        return redirect("/register")
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    admin = request.form["admin"]
    if admin == "admin123":
        admin = True
    else:
        admin = False
    if password1 == password2:
        hash_password = generate_password_hash(password1)
        database_methods.insert_user_password_admin(username,
            hash_password, admin)
        return render_template("index.html")
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        user = session["username"]
    else:
        user = request.form["name"]
        password = request.form["password"]
        #hash_password = generate_password_hash(password)
        hash_password = database_methods.get_hash_password(user)
        if check_password_hash(hash_password, password):    
            session["username"] = user
            session["user_id"] = database_methods.get_id(user)
            admin = database_methods.get_admin(user)
            return render_template("login.html", user=user, admin=admin)
    return redirect("/")

@app.route("/about_to_add", methods=["POST"])
def about_to_add():
    costumer = request.form["costumer"]
    work_type = request.form["work_type"]
    price = request.form["price"]
    status = request.form["status"]
    start_date = request.form["start_date"]
    if len(start_date) != 8:
        return redirect("/add")
    user = session["username"]
    #admin = database_methods.get_admin(user)
    return render_template("about_to_add.html", user=user, costumer=costumer,
        work_type=work_type, price=price, status=status, start_date=start_date)

@app.route("/work_added", methods=["POST"])
def work_added():
    costumer = request.form["costumer"]
    work_type = request.form["work_type"]
    price = request.form["price"]
    status = request.form["status"]
    start_date = request.form["start_date"]
    user = session["username"]
    user_id = database_methods.get_id(user)
    database_methods.insert_work(user_id=user_id, costumer=costumer, work_type=work_type, price=price, status=status, start_date=start_date)
    return render_template("work_added.html", user=user, costumer=costumer,
        work_type=work_type, price=price, status=status, start_date=start_date)

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

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")