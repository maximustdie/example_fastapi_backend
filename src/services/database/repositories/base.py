from abc import ABC
from typing import TypeVar, Type, Callable

from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models import BaseModel

SQLAlchemyModel = TypeVar("SQLAlchemyModel", bound=BaseModel)


class SqlalchemyBaseRepository(ABC):

    def __init__(
            self, session_or_factory: AsyncSession | Callable[[], AsyncSession],
            query_model: Type[SQLAlchemyModel]
    ):
        self._session_or_factory = session_or_factory
        self.model = query_model

    @property
    def session(self) -> AsyncSession:
        if isinstance(self._session_or_factory, AsyncSession):
            return self._session_or_factory
        return self._session_or_factory()
