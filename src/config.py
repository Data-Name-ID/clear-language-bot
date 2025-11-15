from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent  # src


class Settings(BaseSettings):
    api_url: str
    telegram_token: str

    model_config = SettingsConfigDict(
        env_file=(BASE_DIR.parent / ".env", BASE_DIR.parent / ".env.dev"),
        case_sensitive=False,
        env_prefix="BOT__",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings()
