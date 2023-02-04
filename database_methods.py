from db import db

def get_admin(username):
    result = db.session.execute("SELECT admin FROM users WHERE username=:username", {'username':username})
    admin = result.fetchone()
    if admin:
        return "You are admin"
    return "You are not admin"

def get_count_by_costumer(username):
    id_result = db.session.execute("SELECT id FROM users WHERE username=:username", {'username':username})
    id = id_result.fetchone()
    if id is None:
        return 0
    result = db.session.execute("SELECT COUNT(costumer) FROM work WHERE user_id=:id", {'id':id[0]})
    count = result.fetchone()[0]
    return count