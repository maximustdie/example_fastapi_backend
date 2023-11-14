from fastapi_filter.contrib.sqlalchemy import Filter

from api.http.filters.author import AuthorFilter
from dto.author import AuthorCreateDTO, AuthorDTO
from services.database.repositories.author import AuthorRepository


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    async def create_author(self, author: AuthorCreateDTO):
        return await self.author_repository.create(author)

    async def get_authors(self, filters: Filter | None):
        return await self.author_repository.get_all(filters=filters)
