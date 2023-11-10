from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine, async_sessionmaker
from contextvars import ContextVar

from services.database.settings import settings

db_session_context: ContextVar[UUID | None] = ContextVar("db_session_context", default=None)

engine = create_async_engine(settings.POSTGRES.build_url())


def get_db_session_context() -> UUID:
    session_id = db_session_context.get()

    if not session_id:
        raise ValueError("Currently no session is available")

    return session_id


def set_db_session_context(session_id: UUID | None) -> None:
    db_session_context.set(session_id)


AsyncScopedSession = async_scoped_session(
    session_factory=async_sessionmaker(bind=engine, autoflush=False, autocommit=False), scopefunc=get_db_session_context
)


def get_current_session() -> AsyncSession:
    return AsyncScopedSession()
