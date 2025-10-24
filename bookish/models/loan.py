from datetime import datetime, timedelta

from . import db

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    book_isbn = db.Column(db.String(32), db.ForeignKey("books.ISBN"), nullable=False, index=True)
    checked_out_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True, index=True)

    def __init__(self, user_id, book_isbn, checked_out_at=None, due_at=None):
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.checked_out_at = checked_out_at or datetime.utcnow()
        self.due_date = due_at or (datetime.utcnow() + timedelta(days=14))

    def __repr__(self):
        return f"<Loan {self.id} user={self.user_id} book={self.book_isbn}>"

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_isbn": self.book_isbn,
            "checked_out_at": self.checked_out_at.isoformat(),
            "due_date": self.due_date.isoformat(),
            "return_date": self.return_date.isoformat() if self.return_date else None,
        }
