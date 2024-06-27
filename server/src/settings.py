from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    """Base settings class."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    """Settings class."""

    server_host: str = "localhost"
    server_port: int = 8000
    workers: int = 1
    reload: bool = True
    log_level: str = "info"

    env: str = "dev"


settings = Settings()
