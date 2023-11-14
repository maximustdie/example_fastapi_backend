from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select

from api.http.filters.author import AuthorFilter
from dto.author import AuthorDTO, AuthorCreateDTO
from services.database.models import AuthorModel
from services.database.repositories.base import BaseRepository


class AuthorRepository(BaseRepository):
    def __init__(self, query_model, session_or_factory):
        super().__init__(session_or_factory, query_model)

    async def create(self, autor: AuthorCreateDTO):
        author: AuthorModel = self.model(**autor.model_dump())
        self.session.add(author)
        await self.session.flush()
        await self.session.refresh(author)
        return AuthorDTO(**author.as_dict())

    async def get_all(self, filters: Filter | None):
        stmt = select(AuthorModel)
        if filters:
            stmt = filters.filter(stmt)
        result = (await self.session.execute(stmt)).scalars().all()
        return [AuthorDTO(**author.as_dict()) for author in result]


