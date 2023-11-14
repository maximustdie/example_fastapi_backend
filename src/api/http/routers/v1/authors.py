from fastapi import APIRouter, Depends
from fastapi import status

from abstractions.decorators.transactional import transactional
from dto.author import AuthorCreateDTO
from services.authors.author_service import AuthorService
from services.authors.factory import create_author_service

router = APIRouter(tags=["authors"])


@router.post(path="/authors", status_code=status.HTTP_201_CREATED)
@transactional
async def create_author(data: AuthorCreateDTO, autor_service: AuthorService = Depends(create_author_service)):
    autor = await autor_service.create_author(data)
    return autor
