from depends.database import get_current_session
from services.database.models import BookModel
from services.database.repositories.book import BookRepository


def book_repository_factory():
    return BookRepository(query_model=BookModel, session_or_factory=get_current_session())
