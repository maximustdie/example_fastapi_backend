from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from abstractions.decorators.transactional import transactional
from abstractions.services.book import AbstractionBookService
from depends.database import get_current_session
from dto.book import BookCreateDTO, BookDTO
from services.book.factory import book_service_factory
from services.database.models import BookModel

router = APIRouter(tags=["books"])


@router.post("/books")
@transactional
async def create_book(data: BookCreateDTO, book_service: AbstractionBookService = Depends(book_service_factory)):
    book = await book_service.create_book(book=data)
    return book

