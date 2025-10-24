from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bookish.services.books_service import create_book, list_books

def book_routes(app):
    @app.route("/api/books", methods=["GET"])
    def get_books():
        books = list_books()
        results = [
            {
                "title": b.title,
                "authors": b.authors,
                "isbn": b.isbn,
                "total_copies": b.total_copies,
            }
            for b in books
        ]
        return {"books": results}, 200

    @app.route("/api/books", methods=["POST"])
    @jwt_required()
    def post_book():
        _user_id = get_jwt_identity()

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
