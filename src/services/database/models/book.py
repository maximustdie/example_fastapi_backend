from sqlalchemy import Column, UUID, text, VARCHAR, TEXT

from services.database.models.base import BaseModel


class BookModel(BaseModel):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=text("gen_random_uuid()"))
    title = Column(VARCHAR, nullable=False)
    author = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=True, default=None)
