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
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id WHERE user_id=:user_id ORDER BY w.costumer"), {'user_id':user_id[0]})
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_count_by_costumer_admin():
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id ORDER BY w.costumer"))
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
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id WHERE user_id=:user_id ORDER BY w.price DESC"), {'user_id':user_id[0]})
    price_list = result.fetchall()
    if price_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    price_list_length = result.fetchone()[0]
    return price_list, price_list_length

def get_count_by_price_admin():
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id ORDER BY w.price DESC"))
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
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id WHERE user_id=:user_id ORDER BY w.work_type"), {'user_id':user_id[0]})
    work_list = result.fetchall()
    if work_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(work_type) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    work_list_length = result.fetchone()[0]
    return work_list, work_list_length

def get_count_by_work_type_admin():
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id ORDER BY w.work_type"))
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
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id WHERE user_id=:user_id ORDER BY w.date DESC"), {'user_id':user_id[0]})
    date_list = result.fetchall()
    if date_list is None:
        return [], 0
    result = db.session.execute(text("SELECT COUNT(costumer) FROM work WHERE user_id=:user_id"), {'user_id':user_id[0]})
    date_list_length = result.fetchone()[0]
    return date_list, date_list_length

def get_count_by_date_admin():
    result = db.session.execute(text("SELECT w.id, w.costumer, w.work_type, w.price, w.status, w.date, u.username FROM work w LEFT JOIN users u ON w.user_id=u.id ORDER BY w.date DESC"))
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
    if modify_list is None:
        return []
    return modify_list

def get_notes():
    result = db.session.execute(text("SELECT id, time, memo FROM notes ORDER BY time DESC"))
    notes_gathered = result.fetchall()
    if notes_gathered is None:
        return []
    return notes_gathered

def get_one_note(id):
    result = db.session.execute(text("SELECT id, time, memo FROM notes WHERE id=:id"), {"id":id})
    note_gathered = result.fetchall()
    return note_gathered

def get_comments_and_commenters(notes_id):
    result = db.session.execute(text("SELECT c.comment, c.time, u.username FROM comments c LEFT JOIN users u ON c.user_id=u.id WHERE c.notes_id=:notes_id ORDER BY c.time DESC"), {"notes_id":notes_id})
    gathered = result.fetchall()
    if gathered is None:
        return []
    return gathered

def insert_note(user_id, memo):
    db.session.execute(text("INSERT INTO notes (user_id, time, memo) VALUES (:user_id, NOW(), :memo)"),
                       {"user_id":user_id, "memo":memo})
    db.session.commit()

def insert_comment(user_id, notes_id, comment):
    db.session.execute(text("INSERT INTO comments (user_id, notes_id, time, comment) VALUES (:user_id, :notes_id, NOW(), :comment)"),
                       {"user_id":user_id, "notes_id":notes_id, "comment":comment})
    db.session.commit()

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

def search_by_given(costumer_search, date_search, user_id):
    if date_search is "":
        date_search = "1950"
        second_date = "2049"
    else:
        second_date = int(date_search) + 1
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE user_id=:user_id AND costumer LIKE :costumer_search AND date >= :date_search AND date < :second_date"),
                        {"costumer_search":"%"+costumer_search+"%", "date_search":date_search+"-01-01", "second_date":str(second_date)+"-01-01", "user_id":user_id})
    found = result.fetchall()
    return found

def search_by_given_admin(costumer_search, date_search):
    if date_search is "":
        date_search = "1950"
        second_date = "2049"
    else:
        second_date = int(date_search) + 1
    result = db.session.execute(text("SELECT id, costumer, work_type, price, status, date FROM work WHERE costumer LIKE :costumer_search AND date >= :date_search AND date < :second_date"),
                        {"costumer_search":"%"+costumer_search+"%", "date_search":date_search+"-01-01", "second_date":str(second_date)+"-01-01"})
    found = result.fetchall()
    return found

def good_password(password):
    if len(password) > 7 and bool(re.search(r'[a-z]', password)) is True and bool(re.search(r'[A-Z]', password)) is True and bool(re.search(r'[0-9]', password)) is True:
        return True
