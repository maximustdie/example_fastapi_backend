from services.database.models import AuthorModel
from services.database.repositories.base import BaseRepository


class AuthorRepository(BaseRepository):
    def __init__(self, query_model, session_or_factory):
        super().__init__(session_or_factory, query_model)

    async def create(self, **autor_data):
        model: AuthorModel = self.model(**autor_data)
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return model.as_dict()
