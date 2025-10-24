from bookish.controllers.bookish import bookish_routes
from bookish.controllers.books_controller import book_routes
from .auth_controller import bp as auth_bp

def register_controllers(app):
    app.register_blueprint(auth_bp)
    bookish_routes(app)
    book_routes(app)
