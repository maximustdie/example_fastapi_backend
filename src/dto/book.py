from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BookDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str


class BookCreateDTO(BaseModel):
    title: str
