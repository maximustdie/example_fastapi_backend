from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AuthorDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    first_name: str
    last_name: str


class AuthorCreateDTO(BaseModel):
    author_id: UUID
    first_name: str
    last_name: str
