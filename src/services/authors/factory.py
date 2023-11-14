from services.authors.author_service import AuthorService
from services.database.repositories.factories.author import create_author_repository


def create_author_service():
    return AuthorService(author_repository=create_author_repository())
