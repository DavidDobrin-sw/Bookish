from datetime import datetime, timedelta

from . import db

class Book(db.Model):
    __tablename__ = "books"

    isbn = db.Column("ISBN", db.String(32), primary_key=True)
    title = db.Column(db.String(300), nullable=False, index=True)
    authors = db.Column(db.String(500), nullable=False)
    total_copies = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, isbn, title, authors, total_copies=1):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.total_copies = total_copies

    def __repr__(self):
        return f"<Book {self.isbn} {self.title}>"

    def serialize(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "authors": self.authors,
            "total_copies": self.total_copies,
            "created_at": self.created_at.isoformat(),
        }