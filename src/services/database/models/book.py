from sqlalchemy import Column, UUID, text, VARCHAR, TEXT, ForeignKey
from sqlalchemy.orm import relationship

from services.database.models.base import BaseModel


class BookModel(BaseModel):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=text("gen_random_uuid()"))
    title = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=True, default=None)
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id"), nullable=False)

    author = relationship("AuthorModel", back_populates="books")
