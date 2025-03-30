from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class BotConfig(BaseModel):
    token: str


class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    bc: BotConfig
    db: DatabaseConfig


setting = Setting()
