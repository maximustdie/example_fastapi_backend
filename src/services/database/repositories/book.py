from typing import Any
from uuid import UUID

from sqlalchemy import select

from abstractions.repositories.book import AbstractionBookRepository
from dto.book import BookDTO, BookCreateDTO
from services.database.models import BookModel
from services.database.repositories.base import SqlalchemyBaseRepository


class AuthorRepository(SqlalchemyBaseRepository, AbstractionBookRepository):

    def __init__(self, query_model, session_or_factory):
        super().__init__(session_or_factory, query_model)

    # TODO: Что нужно принимать и возвращать в итоге DTO, словарь или модель. Мой мне кажется DTO
    async def create(self, obj: BookCreateDTO) -> Any:
        book: BookModel = self.model(**obj.model_dump())
        self.session.add(book)
        await self.session.flush()
        await self.session.refresh(book)
        return BookDTO(**book.as_dict())

    async def get_by_id(self, obj_id: UUID) -> Any:
        pass

    async def get_list(self, **filters) -> Any:
        stmt = select(BookModel)
        result = (await self.session.execute(stmt)).scalars().all()
        return [BookDTO(**author.as_dict()) for author in result]

    async def update(self, obj_id: UUID, **values) -> None:
        pass

    async def delete(self, obj_id: UUID, **values) -> None:
        pass