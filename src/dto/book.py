from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BookDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    author_id: UUID
    title: str
    description: str | None = None


class BookCreateDTO(BaseModel):
    author_id: UUID
    title: str
    description: str | None = None
