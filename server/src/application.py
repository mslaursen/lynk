from contextlib import asynccontextmanager
from typing import AsyncIterator

from db.db_lifetime import setup_db, shutdown_db
from fastapi import FastAPI
from loguru import logger
from routes import base_router
from settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application startup and shutdown events."""

    setup_db(app)

    yield

    await shutdown_db(app)


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.
    """

    if settings.env == "dev":
        logger.info(settings.model_dump_json(indent=2))

    app = FastAPI(
        root_path="/api",
        lifespan=lifespan,
    )

    app.include_router(base_router)

    return app
