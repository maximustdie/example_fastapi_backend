from dto.author import AuthorCreateDTO, AuthorDTO
from services.database.repositories.author import AuthorRepository


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    async def create_author(self, author: AuthorCreateDTO):
        result: dict = await self.author_repository.create(**author.model_dump())
        return AuthorDTO(**result)
