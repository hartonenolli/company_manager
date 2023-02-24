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
    if database_methods.good_password(password1) is True:
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
        hash_password = database_methods.get_hash_password(user)
        if not check_password_hash(hash_password, password):
            return redirect("/")
        session["username"] = user
        session["user_id"] = database_methods.get_id(user)
    admin = database_methods.get_admin(user)
    return render_template("login.html", user=user, admin=admin)
    

@app.route("/about_to_add", methods=["POST"])
def about_to_add():
    costumer = request.form["costumer"]
    work_type = request.form["work_type"]
    price = request.form["price"]
    status = request.form["status"]
    date = request.form["date"]
    user = session["username"]
    return render_template("about_to_add.html", user=user, costumer=costumer,
        work_type=work_type, price=price, status=status, date=date)

@app.route("/work_added", methods=["POST"])
def work_added():
    costumer = request.form["costumer"]
    work_type = request.form["work_type"]
    price = request.form["price"]
    status = request.form["status"]
    date = request.form["date"]
    user = session["username"]
    user_id = database_methods.get_id(user)
    database_methods.insert_work(user_id=user_id, costumer=costumer, work_type=work_type, price=price, status=status, date=date)
    return render_template("work_added.html", user=user, costumer=costumer,
        work_type=work_type, price=price, status=status, date=date)

@app.route("/search")
def search():

    return render_template("search.html")

@app.route("/add")
def add():

    return render_template("add.html")

@app.route("/info", methods=["POST"])
def info():
    intrest = request.form["intrest"]
    # idea to use sql = f"SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY {intrest}"
    # I try to implement this when time
    # This way it would be possible to use database_methods like so:
    # database_method.get_count(session["username"], sql)
    if "admin" not in intrest:
        if intrest == "costumer":
            count = database_methods.get_count_by_costumer(session["username"])
        elif intrest == "price":
            count = database_methods.get_count_by_price(session["username"])
        elif intrest == "work_type":
            count = database_methods.get_count_by_work_type(session["username"])
        elif intrest == "date":
            count = database_methods.get_count_by_date(session["username"])
        number_of_intrest = count[1]
        intrest_list = count[0]
        combined_price = database_methods.get_combined_price(session["username"])
        return render_template("info_gathered.html", intrest=intrest, intrest_list=intrest_list, number_of_intrest=number_of_intrest, combined_price=combined_price)
    if not database_methods.get_admin(session["username"]):
        return redirect("/login")
    if intrest == "costumer_admin":
        count = database_methods.get_count_by_costumer_admin()
    elif intrest == "price_admin":
        count = database_methods.get_count_by_price_admin()
    elif intrest == "work_type_admin":
        count = database_methods.get_count_by_work_type_admin()
    elif intrest == "date_admin":
        count = database_methods.get_count_by_date_admin()
    number_of_intrest = count[1]
    intrest_list = count[0]
    combined_price = database_methods.get_combined_price_admin()
    return render_template("info_gathered.html", intrest=intrest, intrest_list=intrest_list, number_of_intrest=number_of_intrest, combined_price=combined_price)

    
@app.route("/modify")
def modify():

    return render_template("modify.html")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/")