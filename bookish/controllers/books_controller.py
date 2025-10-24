from flask import request
from bookish.models import db
from bookish.models.book import Book


def book_routes(app):
    @app.route("/api/books", methods=["GET", "POST"])
    def handle_books():
        if request.method == "POST":
            if not request.is_json:
                return {"error": "The request payload is not in JSON format"}, 415

            data = request.get_json()

            book = Book(
                title=data["title"],
                authors=data["authors"],
                isbn=data["isbn"],
                total_copies=int(data.get("total_copies", 1)),
            )

            db.session.add(book)
            db.session.commit()


            return {
                "message": "Book created",
                "book": {
                    "title": book.title,
                    "authors": book.authors,
                    "isbn": book.isbn,
                    "total_copies": book.total_copies,
                },
            }, 201

        elif request.method == "GET":
            books = Book.query.all()
            results = [
                {
                    "title": book.title,
                    "authors": book.authors,
                    "isbn": book.isbn,
                    "total_copies": book.total_copies,
                } for book in books]
            return {"books": results}

