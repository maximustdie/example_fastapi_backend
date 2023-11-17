from fastapi import Depends

from services.book.book import BookService
from services.database.repositories.book import BookRepository
from services.database.repositories.factories.book import book_repository_factory


# TODO: Должен тайпить интерфейс или конкретику?
def book_service_factory(
    book_repository: BookRepository = Depends(book_repository_factory),
):
    return BookService(book_repository=book_repository)
