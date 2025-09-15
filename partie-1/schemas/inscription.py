import json
from pydantic import BaseModel, field_validator, ConfigDict


class InscriptionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    annee_etude: int
    matricule: str
    cours_json: list
    nom: str
    prenom: str

    # Have cours_json be a list before sending it back to the client
    @field_validator("cours_json", mode="before")
    def parse_json(cls, cours_json) -> list:
        return json.loads(cours_json)
