import uvicorn
from settings import settings


def main() -> None:
    """Entrypoint of the application."""

    uvicorn.run(
        "application:get_app",
        host=settings.server_host,
        port=settings.server_port,
        workers=settings.workers,
        reload=settings.reload,
        log_level=settings.log_level,
        factory=True,
        lifespan="on",
        proxy_headers=True,
        forwarded_allow_ips="*",
    )


if __name__ == "__main__":
    main()
