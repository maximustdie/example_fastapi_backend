from typing import List, Any
from uuid import UUID

from abstractions.repositories.book import AbstractionBookRepository
from abstractions.services.book import AbstractionBookService
from dto.book import BookDTO, BookCreateDTO


class BookService(AbstractionBookService):
    def __init__(self, book_repository: AbstractionBookRepository):
        super().__init__(book_repository)

    async def create_book(self, book: BookCreateDTO) -> Any:
        book = await self.book_repository.create(obj=book)
        return book

    async def get_book_by_id(self, book_id: UUID) -> BookDTO:
        pass

    async def get_list_book(self, **filters) -> List[BookDTO]:
        pass

    async def update_book_by_id(self, book_id: UUID, **values) -> None:
        pass

    async def delete_book_by_id(self, book_id: UUID) -> None:
        pass
