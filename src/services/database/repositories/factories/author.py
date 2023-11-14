from depends.database import get_current_session
from services.database.models.author import AuthorModel
from services.database.repositories.author import AuthorRepository


def create_author_repository():
    return AuthorRepository(query_model=AuthorModel, session_or_factory=get_current_session())


