from db import db
from sqlalchemy.sql import text
import re

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
    user_id = id_result.fetchone()
    if user_id is None:
        return [], 0
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY costumer"), {'user_id':user_id[0]})
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_count_by_price(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    user_id = id_result.fetchone()
    if user_id is None:
        return [], 0
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY price DESC"), {'user_id':user_id[0]})
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_count_by_price_admin():
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY price DESC"), {'user_id':user_id[0]})
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work"))
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_count_by_work_type(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    user_id = id_result.fetchone()
    if user_id is None:
        return [], 0
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY work_type"), {'user_id':user_id[0]})
    work_list = result.fetchall()
    if work_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(work_type) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    work_list_length = result.fetchone()[0]
    return work_list, work_list_length

def get_count_by_date(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    user_id = id_result.fetchone()
    if user_id is None:
        return [], 0
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id ORDER BY date DESC"), {'user_id':user_id[0]})
    date_list = result.fetchall()
    if date_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    date_list_length = result.fetchone()[0]
    return date_list, date_list_length

def get_combined_price(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    id = id_result.fetchone()
    if id is None:
        return 0
    result = db.session.execute(text("SELECT SUM(price) FROM work WHERE user_id=:id"), {'id':id[0]})
    combined_price = result.fetchone()[0]
    return combined_price

def insert_user_password_admin(username, password, admin):
    db.session.execute(text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"), {"username":username, "password":password, "admin":admin})
    db.session.commit()

def insert_work(user_id, costumer, work_type, price, status, date):
    db.session.execute(text("INSERT INTO work (user_id, costumer, work_type, price, status, date) VALUES (:user_id, :costumer, :work_type, :price, :status, :date)"),
                       {"user_id":user_id, "costumer":costumer, "work_type":work_type, "price":price, "status":status, "date":date})
    db.session.commit()

def good_password(password):
    if len(password) > 7 and bool(re.search(r'[a-z]', password)) is True and bool(re.search(r'[A-Z]', password)) is True and bool(re.search(r'[0-9]', password)) is True:
        return True
