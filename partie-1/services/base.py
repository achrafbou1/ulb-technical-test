from typing import TypeVar, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db import Base

# Generic type for models
Model = TypeVar("Model", bound=Base)

class BaseService:
    _model: type[Model]
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all(self) -> Sequence[Model]:
        query = await self.db.execute(select(self._model))
        return  query.scalars().all()