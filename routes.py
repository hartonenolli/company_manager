from app import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/log_in", methods=["POST"])
def log_in():
    user = request.form["name"]
    return render_template("log_in.html", user=user)