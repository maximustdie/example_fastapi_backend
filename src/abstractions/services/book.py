from abc import ABC, abstractmethod
from typing import List, Any
from uuid import UUID

from abstractions.repositories.book import AbstractionBookRepository
from dto.book import BookDTO


class AbstractionBookService(ABC):

    # TODO: Нужно ли тайпить тип репозитория (AbstractRepository | AbstractBookRepository) или нет
    def __init__(self, book_repository: AbstractionBookRepository):
        self.book_repository = book_repository

    @abstractmethod
    async def create_book(self, book) -> Any:
        pass

    @abstractmethod
    async def get_book_by_id(self, book_id: UUID) -> BookDTO:
        pass

    @abstractmethod
    # TODO: Как правильно тайпить фильтры в аргументах этого метода?
    async def get_list_book(self, **filters) -> List[BookDTO]:
        pass

    @abstractmethod
    async def update_book_by_id(self, book_id: UUID, **values) -> None:
        pass

    @abstractmethod
    async def delete_book_by_id(self, book_id: UUID) -> None:
        pass
