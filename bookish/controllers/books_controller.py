from flask import request
from bookish.services.books_service import create_book, list_books

def book_routes(app):
    @app.route("/api/books", methods=["GET", "POST"])
    def handle_books():
        if request.method == "POST":
            if not request.is_json:
                return {"error": "The request payload is not in JSON format"}, 415

            data = request.get_json()
            book = create_book(data)

            return {
                "message": "Book created",
                "book": {
                    "title": book.title,
                    "authors": book.authors,
                    "isbn": book.isbn,
                    "total_copies": book.total_copies,
                },
            }, 201

        elif request.method == 'GET':
            books = list_books()
            results = [
                {
                    "title": book.title,
                    "authors": book.authors,
                    "isbn": book.isbn,
                    "total_copies": book.total_copies,
                }
                for book in books
            ]
            return {"books": results}
        return None