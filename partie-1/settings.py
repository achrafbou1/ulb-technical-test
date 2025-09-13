from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./universite_demo.sqlite"
    API_VERSION: int = 1

settings = Settings()