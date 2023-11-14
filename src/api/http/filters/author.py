from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from services.database.models import AuthorModel


class AuthorFilter(Filter):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Constants(Filter.Constants):
        model = AuthorModel

