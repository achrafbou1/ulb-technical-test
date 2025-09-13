from sqlalchemy import select

from models.note import Note
from services.base import BaseService


class NoteService(BaseService):
    _model = Note

    async def get_by_id(self, id: int) -> Note | None:
        query = await self.db.execute(select(Note).where(Note.id == id))
        return query.scalar_one_or_none()
