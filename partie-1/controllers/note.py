from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_db
from schemas.note import NoteOut
from services.note import NoteService

router = APIRouter(prefix="/note", tags=["note"])


@router.get("/", response_model=list[NoteOut])
async def get_notes(db=Depends(get_db)):
    note_service = NoteService(db)
    return await note_service.get_all()

@router.get("/{id_}", response_model=NoteOut)
async def get_by_id(id_: int, db=Depends(get_db)):
    note_service = NoteService(db)
    note = await note_service.get_by_id(id_)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note