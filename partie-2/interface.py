from typing import TypeVar, Type

import requests
from pydantic import BaseModel, TypeAdapter

from schemas.cours import CoursResponse
from schemas.inscription import InscriptionResponse
from schemas.note import NoteResponse
from settings import settings


class PsyelAPIInterface:
    """Cette classe permet d'intéragir avec l'API Psyel et permet aussi de gérer
    une session permanente vers le service.

    Attributes:
        _session (requests.Session): Session persistente.
    """

    T = TypeVar("T", bound=BaseModel)  # variable de type générique pour toute sous-classes de BaseModel,
    _session: requests.Session

    def __init__(self):
        self._session = requests.Session()

    @property
    def _cours_endpoint(self):
        return f"{settings.API_URL}/cours"

    @property
    def _inscription_endpoint(self):
        return f"{settings.API_URL}/inscriptions"

    @property
    def _note_endpoint(self):
        return f"{settings.API_URL}/notes"

    def _do_request(self, url: str, response_schema: Type[T]) -> list[T]:
        res = self._session.get(url)
        res.raise_for_status()
        res = res.json()
        return TypeAdapter(list[response_schema]).validate_python(res)

    def get_all_cours(self) -> list[CoursResponse]:
        return self._do_request(f"{self._cours_endpoint}", CoursResponse)

    def get_all_inscriptions(self) -> list[InscriptionResponse]:
        return self._do_request(f"{self._inscription_endpoint}", InscriptionResponse)

    def get_all_notes(self) -> list[NoteResponse]:
        return self._do_request(f"{self._note_endpoint}", NoteResponse)