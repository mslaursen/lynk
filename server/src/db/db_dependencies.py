from typing import AsyncGenerator

from fastapi import FastAPI, Request
from sqlalchemy import exc as sa_exc
from sqlalchemy.ext.asyncio import AsyncSession


def setup_sa(
    app: FastAPI,
) -> None:
    """Setup database engine."""


async def shutdown_sa(
    app: FastAPI,
) -> None:
    """Shutdown database engine."""


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """Get a database session."""
    session: AsyncSession = request.app.state.db_session_factory()

    try:
        yield session
    except sa_exc.DBAPIError:
        await session.rollback()
        raise
    finally:
        await session.commit()
        await session.close()
