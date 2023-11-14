from services.database.repositories.book import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository
