from datetime import datetime, timedelta

from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

    def serialize(self):
        return {"id": self.id, "email": self.email, "created_at": self.created_at.isoformat()}
