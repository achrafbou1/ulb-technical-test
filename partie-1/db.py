from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import settings

# SQLite engine
engine = create_async_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
)

AsyncSessionLocal = async_sessionmaker(
    engine, autocommit=False, autoflush=False, expire_on_commit=False
)


# Base class for models
class Base(DeclarativeBase):
    pass


# Used later for reflecting existing tables
metadata = MetaData()

db = AsyncSessionLocal()
