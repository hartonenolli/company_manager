from db import db
from sqlalchemy.sql import text
import re

def get_admin(username):
    result = db.session.execute(text("SELECT admin FROM users WHERE username=:username"), {'username':username})
    admin = result.fetchone()[0]
    if admin == True:
        return "You are admin"
    return "You are not admin"

def get_id(username):
    result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    user_id = result.fetchone()[0]
    return user_id

def get_user_id_with_work_id(id):
    result = db.session.execute(text("SELECT user_id FROM work WHERE id=:id"), {'id':id})
    user_id = result.fetchone()[0]
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

def get_one_work_with_id(id):
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE id=:id"), {'id':id})
    selected_work = result.fetchall()
    return selected_work

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

def get_count_by_costumer_admin():
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work ORDER BY costumer"))
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work"))
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
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work ORDER BY price DESC"))
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

def get_count_by_work_type_admin():
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work ORDER BY work_type"))
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work"))
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

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

def get_count_by_date_admin():
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work ORDER BY date DESC"))
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work"))
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_combined_price(username):
    id_result = db.session.execute(text("SELECT id FROM users WHERE username=:username"), {'username':username})
    id = id_result.fetchone()
    if id is None:
        return 0
    result = db.session.execute(text("SELECT SUM(price) FROM work WHERE user_id=:id"), {'id':id[0]})
    combined_price = result.fetchone()[0]
    return combined_price

def get_combined_price_admin():
    result = db.session.execute(text("SELECT SUM(price) FROM work"))
    combined_price = result.fetchone()[0]
    return combined_price

def get_work_history(work_id):
    result = db.session.execute(text("SELECT id, user_id, modifier, explination, time, costumer, work_type, price, status, date FROM modify WHERE work_id=:work_id ORDER BY time DESC"), {'work_id':work_id})
    modify_list = result.fetchall()
    #result = db.session.execute(text("SELECT user_id FROM work WHERE id=:id"), {'id':id})
    if modify_list is None:
        return []
    return modify_list

def insert_user_password_admin(username, password, admin):
    db.session.execute(text("INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"), {"username":username, "password":password, "admin":admin})
    db.session.commit()

def insert_work(user_id, costumer, work_type, price, status, date):
    db.session.execute(text("INSERT INTO work (user_id, costumer, work_type, price, status, date) VALUES (:user_id, :costumer, :work_type, :price, :status, :date)"),
                       {"user_id":user_id, "costumer":costumer, "work_type":work_type, "price":price, "status":status, "date":date})
    db.session.commit()

def insert_modify_copy_of_work(id, modifier, work_id, explination):
    result = db.session.execute(text("SELECT costumer FROM work WHERE id=:id"), {'id':work_id})
    costumer = result.fetchone()[0]
    result = db.session.execute(text("SELECT work_type FROM work WHERE id=:id"), {'id':work_id})
    work_type = result.fetchone()[0]
    result = db.session.execute(text("SELECT price FROM work WHERE id=:id"), {'id':work_id})
    price = result.fetchone()[0]
    result = db.session.execute(text("SELECT status FROM work WHERE id=:id"), {'id':work_id})
    status = result.fetchone()[0]
    result = db.session.execute(text("SELECT date FROM work WHERE id=:id"), {'id':work_id})
    date = result.fetchone()[0]
    db.session.execute(text("INSERT INTO modify (user_id, modifier, work_id, explination, time, costumer, work_type, price, status, date) VALUES (:user_id, :modifier, :work_id, :explination, NOW(), :costumer, :work_type, :price, :status, :date)"),
                       {"user_id":id, "modifier":modifier, "work_id":work_id, "explination":explination, "costumer":costumer, "work_type":work_type, "price":price, "status":status, "date":date})
    db.session.commit()

def update_work(work_id, costumer, work_type, price, status, date):
    db.session.execute(text("UPDATE work SET costumer=:costumer, work_type=:work_type, price=:price, status=:status, date=:date WHERE id=:id"),
                       {"id":work_id, "costumer":costumer, "work_type":work_type, "price":price, "status":status, "date":date})
    db.session.commit()

def search_by_given(costumer_search, date_search):
    if date_search is "":
        date_search = "1950"
        second_date = "2049"
    else:
        second_date = int(date_search) + 1
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE costumer LIKE :costumer_search AND date >= :date_search AND date < :second_date"),
                        {"costumer_search":"%"+costumer_search+"%", "date_search":date_search+"-01-01", "second_date":str(second_date)+"-01-01"})
    found = result.fetchall()
    #WHERE
    #  login_date >= '2014-02-01'
  #AND login_date <  '2014-03-01'
    #result_2 = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE date=:date_search"),
    #                        {"date_search":date_search})
    #found_date = result_2.fetchall()
    #for i, work in enumerate(found_costumer, 0):
    #    if work.id not in found_date:
    #        found_date.pop(i)
    return found

def good_password(password):
    if len(password) > 7 and bool(re.search(r'[a-z]', password)) is True and bool(re.search(r'[A-Z]', password)) is True and bool(re.search(r'[0-9]', password)) is True:
        return True
