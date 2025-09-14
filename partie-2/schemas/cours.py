from pydantic import BaseModel, Field

class CoursResponse(BaseModel):
    mnemonique: str = Field(pattern=r'^[A-Z]{3}\d{3}$')
    credit: int
    intitule: str
    titulaire: str