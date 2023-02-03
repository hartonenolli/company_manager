from db import db

def get_admin(username):
    result = db.session.execute("SELECT admin FROM users WHERE username=:username", {'username':username})
    admin = result.fetchone()
    if admin:
        return "You are admin"
    return "You are not admin"