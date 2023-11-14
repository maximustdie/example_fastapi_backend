from services.database.repositories.base import BaseRepository


class AuthorRepository(BaseRepository):
    def __init__(self, query_model, session_or_factory):
        super().__init__(session_or_factory, query_model)
