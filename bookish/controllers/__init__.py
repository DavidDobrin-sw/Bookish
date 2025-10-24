from bookish.controllers.bookish import bookish_routes
from bookish.controllers.books_controller import book_routes

def register_controllers(app):
    bookish_routes(app)
    book_routes(app)
