from pydantic import BaseModel, ConfigDict, constr, Field


class NoteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    matricule: str
    mnemonique: str = Field(pattern=r'^[A-Z]{3}\d{3}$')
    note: int