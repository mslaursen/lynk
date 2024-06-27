from fastapi import FastAPI


def setup_db(app: FastAPI) -> None:
    """Setup the database."""


async def shutdown_db(app: FastAPI) -> None:
    """Close the database."""
