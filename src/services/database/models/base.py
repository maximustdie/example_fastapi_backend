from typing import Any, Dict, Iterable, Optional

from sqlalchemy.orm.decl_api import DeclarativeBase


class BaseModel(DeclarativeBase):

    def as_dict(self, include: Optional[Iterable] = None, exclude: Optional[Iterable] = None) -> Dict[Any, Any]:
        return self._get_attributes(include=include, exclude=exclude)

    def _get_attributes(self, include: Optional[Iterable] = None, exclude: Optional[Iterable] = None) -> Dict[Any, Any]:
        if include == exclude and include is not None:
            raise ValueError("Only exclude or include, not both")
        if include:
            return {
                field_name: column_value
                for field_name, column_value in self.__dict__.items()
                if not field_name.startswith("_") and field_name in include
            }
        if exclude:
            return {
                field_name: column_value
                for field_name, column_value in self.__dict__.items()
                if not field_name.startswith("_") and field_name not in exclude
            }
        return {
            field_name: column_value
            for field_name, column_value in self.__dict__.items()
            if not field_name.startswith("_")
        }
