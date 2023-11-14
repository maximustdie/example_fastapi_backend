from services.database.repositories.author import AuthorRepository


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository
