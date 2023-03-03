from app import app
from flask import render_template, request, redirect, session
import database_methods
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

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
        session["csrf_token"] = secrets.token_hex(16)
    admin = database_methods.get_admin(user)
    notes_gathered = database_methods.get_notes()
    return render_template("login.html", user=user, admin=admin, notes_gathered=notes_gathered)

@app.route("/login_note", methods=["POST"])
def login_note():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    memo = request.form["note"]
    database_methods.insert_note(user_id=session["user_id"], memo=memo)
    admin = database_methods.get_admin(session["username"])
    notes_gathered = database_methods.get_notes()
    return render_template("login.html", user=session["username"], admin=admin, notes_gathered=notes_gathered)

@app.route("/comment_note", methods=["POST"])
def comment_note():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    id = request.form["selected"]
    note_gathered = database_methods.get_one_note(id=id)
    note_comments = database_methods.get_comments_and_commenters(notes_id=id)
    return render_template("comment_note.html", note_gathered=note_gathered, note_comments=note_comments)

@app.route("/note_commented", methods=["POST"])
def note_commented():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    id = request.form["selected"]
    comment = request.form["comment_for_note"]
    database_methods.insert_comment(user_id=session["user_id"], notes_id=id, comment=comment)
    note_gathered = database_methods.get_one_note(id=id)
    note_comments = database_methods.get_comments_and_commenters(notes_id=id)
    return render_template("comment_note.html", note_gathered=note_gathered, note_comments=note_comments)
    

@app.route("/about_to_add", methods=["POST"])
def about_to_add():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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

@app.route("/search_by", methods=["GET"])
def search_by():
    costumer_search = request.args["costumer"]
    date_search = request.args["date"]
    if database_methods.get_admin(username=session["username"]) == "You are not admin":
        found = database_methods.search_by_given(costumer_search=costumer_search, date_search=date_search, user_id=session["user_id"])
    else:
        found = database_methods.search_by_given_admin(costumer_search=costumer_search, date_search=date_search)
    return render_template("search_by.html", found=found)

@app.route("/add")
def add():

    return render_template("add.html")

@app.route("/info", methods=["POST"])
def info():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
    if database_methods.get_admin(session["username"]) == "You are not admin":
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

    
@app.route("/modify", methods=["POST"])
def modify():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    work_id = request.form["selected"]
    selected_work = database_methods.get_one_work_with_id(work_id)
    work_history = database_methods.get_work_history(work_id=work_id)
    return render_template("modify.html", selected_work=selected_work, work_history=work_history)

@app.route("/modify_done", methods=["POST"])
def modify_done():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    modifier = database_methods.get_id(session["username"])
    work_id = request.form["work_id"]
    id = database_methods.get_user_id_with_work_id(work_id)
    explination = request.form["explination"]
    costumer = request.form["costumer"]
    work_type = request.form["work_type"]
    price = request.form["price"]
    status = request.form["status"]
    date = request.form["date"]
    database_methods.insert_modify_copy_of_work(id=id,
        modifier=modifier, work_id=work_id, explination=explination)
    database_methods.update_work(work_id=work_id, costumer=costumer,
        work_type=work_type, price=price, status=status, date=date)
    return render_template("modify_done.html")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    del session["csrf_token"]
    return redirect("/")