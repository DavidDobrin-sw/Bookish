from bookish.models import db
from bookish.models.book import Book

def create_book(data):
    book = Book(
        title=data["title"],
        authors=data["authors"],
        isbn=data["isbn"],
        total_copies=int(data.get("total_copies", 1)),
    )
    db.session.add(book)
    db.session.commit()
    return book

def list_books():
    return Book.query.all()