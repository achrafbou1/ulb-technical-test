from pydantic import BaseModel, Field

class NoteResponse(BaseModel):
    id: int
    matricule: str
    mnemonique: str = Field(pattern=r'^[A-Z]{3}\d{3}$')
    note: int