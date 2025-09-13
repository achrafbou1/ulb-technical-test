from pydantic import BaseModel, ConfigDict, Field


class CoursOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    mnemonique: str = Field(pattern=r'^[A-Z]{3}\d{3}$')
    credit: int
    intitule: str
    titulaire: str