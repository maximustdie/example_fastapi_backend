from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from abstractions.decorators.transactional import transactional
from api.http.schemas.response_scheme import PaginatedResponse
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


@router.get("/books", response_model=PaginatedResponse[BookDTO])
@transactional
async def get_all_books_pagination_limit_offset(
    limit: int = Query(100, ge=0), offset: int = Query(0, ge=0), session: AsyncSession = Depends(get_current_session)
):
    stmt = select(BookModel)

    total_count = await session.scalar(select(func.count()).select_from(stmt.subquery()))

    result = (await session.execute(stmt.limit(limit).offset(offset))).scalars().all()
    books = [BookDTO(**book.as_dict()) for book in result]

    return {"total_count": total_count, "items": books}
