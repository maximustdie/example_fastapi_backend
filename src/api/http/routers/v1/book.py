from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from abstractions.decorators.transactional import transactional
from depends.database import get_current_session
from dto.book import BookCreateDTO, BookDTO
from services.database.models import BookModel

router = APIRouter(tags=["books"])


@router.post("/books")
@transactional
async def create_book(data: BookCreateDTO, session: AsyncSession = Depends(get_current_session)):
    book = BookModel(**data.model_dump())
    session.add(book)
    await session.flush()
    await session.refresh(book)
    return BookDTO.model_validate(book)


@router.get("/books")
@transactional
async def get_all_books_pagination_limit_offset(session: AsyncSession = Depends(get_current_session)):
    stmt = select(BookModel)
    result = (await session.execute(stmt)).scalars().all()
    return [BookDTO(**book.as_dict()) for book in result]

