from sqlalchemy import Column, UUID, text, VARCHAR

from services.database.models.base import BaseModel


class BookModel(BaseModel):
    __tablename__ = "suggests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=text("gen_random_uuid()"))
    title = Column(VARCHAR, nullable=False)
