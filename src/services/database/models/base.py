import re
from typing import Any, Dict, Final, Pattern, Type, cast, Iterable, Optional

from sqlalchemy import inspect
from sqlalchemy.orm import declared_attr, has_inherited_table, registry
from sqlalchemy.orm.decl_api import DeclarativeMeta

mapper_registry = registry()

# Регулярное выражение, которое разделяет строку по заглавным буквам
TABLE_NAME_REGEX: Pattern[str] = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])|(?<=[^A-Z])(?=[A-Z])")
PLURAL: Final[str] = "s"


class BaseModel(metaclass=DeclarativeMeta):
    __abstract__ = True
    __mapper_args__ = {"eager_defaults": True}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    registry = mapper_registry
    metadata = mapper_registry.metadata

    @declared_attr
    def __tablename__(self) -> Optional[str]:
        if has_inherited_table(cast(Type[BaseModel], self)):
            return None
        cls_name = cast(Type[BaseModel], self).__qualname__
        table_name_parts = re.split(TABLE_NAME_REGEX, cls_name)
        formatted_table_name = "".join(
            table_name_part.lower() + "_" for i, table_name_part in enumerate(table_name_parts)
        )
        last_underscore = formatted_table_name.rfind("_")
        return formatted_table_name[:last_underscore] + PLURAL

    def as_dict(self, include: Optional[Iterable] = None, exclude: Optional[Iterable] = None) -> Dict[Any, Any]:
        return self._get_attributes(include=include, exclude=exclude)

    def __str__(self) -> str:
        attributes = "|".join(f"{k}:{str(v)}" for k, v in self._get_attributes().items())
        return f"<{self.__class__.__qualname__} {attributes}>"

    def __repr__(self) -> str:
        mapper = inspect(self.__class__)
        primary_keys = " ".join(f"{key.name}={getattr(self, key.name)}" for key in mapper.primary_key)
        return f"{self.__class__.__qualname__}->{primary_keys}"

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
