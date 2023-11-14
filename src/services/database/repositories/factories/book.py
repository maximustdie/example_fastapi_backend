from depends.database import get_current_session
from services.database.models.book import BookModel
from services.database.repositories.book import BookRepository


def create_book_repository():
    return BookRepository(query_model=BookModel, session_or_factory=get_current_session())
