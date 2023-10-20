import functools
import logging
from typing import Callable, Awaitable, Any

from depends.database import get_current_session, get_db_session_context

logger = logging.getLogger(name="transactional")


def transactional(func: Callable[..., Awaitable]) -> Callable[..., Awaitable]:
    @functools.wraps(func)
    async def _wrapper(*args, **kwargs) -> Awaitable[Any]:
        try:
            db_session = get_current_session()

            if db_session.in_transaction():
                return await func(*args, **kwargs)

            async with db_session.begin():
                return_value = await func(*args, **kwargs)

            return return_value

        except Exception as error:
            logger.info(f"Request: {get_db_session_context()}")
            logger.error(error)
            raise

    return _wrapper
