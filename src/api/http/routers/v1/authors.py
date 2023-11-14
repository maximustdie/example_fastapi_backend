from fastapi import APIRouter, Depends
from fastapi import status
from fastapi_filter import FilterDepends

from abstractions.decorators.transactional import transactional
from api.http.filters.author import AuthorFilter
from dto.author import AuthorCreateDTO, AuthorDTO
from services.authors.author_service import AuthorService
from services.authors.factory import create_author_service

router = APIRouter(tags=["authors"])


@router.post(path="/authors", status_code=status.HTTP_201_CREATED)
@transactional
async def create_author(data: AuthorCreateDTO, autor_service: AuthorService = Depends(create_author_service)):
    autor = await autor_service.create_author(data)
    return autor


@router.get(path="/authors", response_model=list[AuthorDTO])
@transactional
async def get_author(
    author_filter: AuthorFilter = FilterDepends(AuthorFilter),
    autor_service: AuthorService = Depends(create_author_service),
):
    return await autor_service.get_authors(filters=author_filter)
