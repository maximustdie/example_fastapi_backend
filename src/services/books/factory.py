from services.books.book_service import BookService
from services.database.repositories.factories.book import create_book_repository


def create_book_service():
    return BookService(book_repository=create_book_repository())
