import uuid

from fastapi import Request, Response, status
from typing import Callable, Awaitable

from starlette.middleware.base import BaseHTTPMiddleware

from depends.database import set_db_session_context, AsyncScopedSession


class DBSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        response = Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            set_db_session_context(session_id=uuid.uuid4())
            response = await call_next(request)

        finally:
            await AsyncScopedSession.remove()
            set_db_session_context(session_id=None)

        return response
