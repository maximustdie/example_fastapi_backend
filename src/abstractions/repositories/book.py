from abc import ABC, abstractmethod
from typing import Any

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractionBookRepository(ABC):

    @abstractmethod
    async def create(self, obj: Any) -> Any:
        pass

    @abstractmethod
    async def get_by_id(self, obj_id: UUID) -> Any:
        pass

    @abstractmethod
    # TODO: Как правильно тайпить фильтры в аргументах этого метода?
    async def get_list(self, **filters) -> Any:
        pass

    @abstractmethod
    async def update(self, obj_id: UUID, **values) -> None:
        pass

    @abstractmethod
    async def delete(self, obj_id: UUID, **values) -> None:
        pass



