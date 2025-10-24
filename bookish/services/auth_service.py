from werkzeug.security import generate_password_hash, check_password_hash
from bookish.models import db
from bookish.models.user import User

def create_user(email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email already registered")
    u = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(u)
    db.session.commit()
    return u

def verify_user(email, password):
    u = User.query.filter_by(email=email).first()
    if not u or not check_password_hash(u.password_hash, password):
        return None
    return u
