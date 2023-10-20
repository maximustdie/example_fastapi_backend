from fastapi import APIRouter, Depends
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
