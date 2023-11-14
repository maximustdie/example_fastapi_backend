import datetime
from typing import TypeVar, Union, Generic, Type, Optional, List, Any, cast, Callable

from sqlalchemy import BinaryExpression, ClauseElement, select, update, exists, delete, func
from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy.orm import joinedload

from services.database.models.base import BaseModel

ASTERISK = "*"

SQLAlchemyModel = TypeVar("SQLAlchemyModel", bound=BaseModel)
ExpressionType = Union[BinaryExpression, ClauseElement, bool]


class BaseRepository(Generic[SQLAlchemyModel]):
    model: Type[SQLAlchemyModel]

    def __init__(
        self, session_or_factory: AsyncSession | Callable[[], AsyncSession], query_model: Type[SQLAlchemyModel] = None
    ) -> None:
        self._session_or_factory = session_or_factory
        self.model = query_model or self.model

    @property
    def session(self) -> AsyncSession:
        if isinstance(self._session_or_factory, AsyncSession):
            return self._session_or_factory
        return self._session_or_factory()
