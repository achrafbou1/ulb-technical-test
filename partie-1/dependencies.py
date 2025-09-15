from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from db import AsyncSessionLocal


# This ensures each request gets its own session
async def get_db() -> Generator[AsyncSession, None, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
