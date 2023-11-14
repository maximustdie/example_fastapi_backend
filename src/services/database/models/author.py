from sqlalchemy import Column, UUID, text, VARCHAR
from sqlalchemy.orm import relationship

from services.database.models import BaseModel


class AuthorModel(BaseModel):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=text("gen_random_uuid()"))
    first_name = Column(VARCHAR, nullable=False)
    last_name = Column(VARCHAR, nullable=False)

    books = relationship("BookModel", back_populates="author")
