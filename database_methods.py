from db import db
from sqlalchemy.sql import text
#from werkzeug.security import check_password_hash, generate_password_hash

def get_admin(username):
    result = db.session.execute(text("SELECT admin FROM users WHERE username=:username"), {'username':username})
    admin = result.fetchone()
    if admin:
        return "You are admin"
    return "You are not admin"

def get_id(username):
    result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    user_id = result.fetchone()[0]
    #user_result = db.session.execute(text("SELECT user_id FROM work WHERE user_id=:user_id"), {'user_id':user_id})
    #id = user_result.fetchone()[0]
    return user_id

def get_user(username):
    result = db.session.execute(text("SELECT username FROM users WHERE username=:username"), {'username':username})
    try:
        name = result.fetchone()[0]
    except TypeError:
        return False
    return True

def get_hash_password(username):
    result = db.session.execute(text("SELECT password FROM users WHERE username=:username"), {'username':username})
    password_hash = result.fetchone()[0]
    return password_hash

def get_count_by_costumer(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    id = id_result.fetchone()
    if id is None:
        return 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:id"), {'id':id[0]})
    count = result.fetchone()[0]
    return count

def get_work_type(user_id):
    result = db.session.execute(text("SELECT work_type, price FROM work WHERE user_id=3 ORDER BY price DESC"), {'user_id':user_id})
    work_list = result.fetchall()
    if work_list is None:
        return 0
    return work_list


def insert_user_password_admin(username, password, admin):
    db.session.execute(text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"), {"username":username, "password":password, "admin":admin})
    db.session.commit()

def insert_work(user_id, costumer, work_type, price, status, start_date):
    db.session.execute(text("INSERT INTO work (user_id, costumer, work_type, price, status, start_date) VALUES (:user_id, :costumer, :work_type, :price, :status, :start_date)"),
                       {"user_id":user_id, "costumer":costumer, "work_type":work_type, "price":price, "status":status, "start_date":start_date})
    db.session.commit()
