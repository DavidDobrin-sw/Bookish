from datetime import datetime, timedelta

from bookish.app import db

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

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, index=True)
    authors = db.Column(db.String(500), nullable=False)
    isbn = db.Column(db.String(32), unique=True, nullable=False, index=True)
    total_copies = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title, authors, isbn, total_copies=1):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.total_copies = total_copies

    def __repr__(self):
        return f"<Book {self.id} {self.title}>"

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "total_copies": self.total_copies,
            "created_at": self.created_at.isoformat(),
        }

class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False, index=True)
    checked_out_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_at = db.Column(db.DateTime, nullable=False)
    returned_at = db.Column(db.DateTime, nullable=True, index=True)

    def __init__(self, user_id, book_id, due_at=None):
        self.user_id = user_id
        self.book_id = book_id
        self.due_at = due_at or (datetime.utcnow() + timedelta(days=14))

    def __repr__(self):
        return f"<Loan {self.id} user={self.user_id} book={self.book_id}>"

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "checked_out_at": self.checked_out_at.isoformat(),
            "due_at": self.due_at.isoformat(),
            "returned_at": self.returned_at.isoformat() if self.returned_at else None,
        }
