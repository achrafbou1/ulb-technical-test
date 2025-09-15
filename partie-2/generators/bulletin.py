import pandas as pd

from generators.base import BaseGenerator
from interface import PsyelAPIInterface
from schemas.cours import CoursResponse
from schemas.inscription import InscriptionResponse
from schemas.note import NoteResponse
from settings import settings


class BulletinGenerator(BaseGenerator):
    _api: PsyelAPIInterface
    _cours: list[CoursResponse]
    _inscriptions: list[InscriptionResponse]
    _notes: list[NoteResponse]

    # Dataframes
    _cours_df: pd.DataFrame
    _inscriptions_df: pd.DataFrame
    _notes_df: pd.DataFrame
    _bulletin_dataframe: pd.DataFrame

    @classmethod
    def _ects_total_inscrits(cls, group: pd.DataFrame) -> int:
        return int(group["credit"].sum())

    @classmethod
    def _ects_obtenus(cls, group: pd.DataFrame) -> int:
        return int(group.loc[group["note"] >= 10, "credit"].sum())

    @classmethod
    def _moyenne_ponderee(cls, group: pd.DataFrame) -> float:
        grades = group.loc[group["note"].notna()]
        total_credits = grades["credit"].sum()
        if total_credits == 0:
            return 0.0
        return (grades["note"] * grades["credit"]).sum() / total_credits

    def _reussite(self, group: pd.DataFrame) -> bool:
        if self._ects_obtenus(group) >= 60 or (
            group["note"].notna().all()
            and (group["note"] >= 10).all()
            and self._moyenne_ponderee(group) >= 10
        ):
            return True
        return False

    def _details(self, group: pd.DataFrame) -> list[dict]:
        details_list = []
        for row in group.itertuples(index=False):
            details_list.append(
                {
                    "mnemonique": (
                        row.mnemonique if not pd.isna(row.mnemonique) else None
                    ),
                    "intitule": row.intitule if not pd.isna(row.intitule) else None,
                    "credit": int(row.credit) if not pd.isna(row.credit) else 0,
                    "titulaire": row.titulaire if not pd.isna(row.titulaire) else None,
                    "note": row.note if not pd.isna(row.note) else None,
                }
            )
        return details_list

    def __init__(self, api: PsyelAPIInterface):
        self._api = api

    def extract(self):
        self._cours = self._api.get_all_cours()
        self._inscriptions = self._api.get_all_inscriptions()
        self._notes = self._api.get_all_notes()

    def transform(self):
        self._cours_df = pd.DataFrame([course.model_dump() for course in self._cours])
        self._inscriptions_df = pd.DataFrame(
            [inscription.model_dump() for inscription in self._inscriptions]
        )
        self._notes_df = pd.DataFrame([note.model_dump() for note in self._notes])

        # Chaque cours dans une ligne différente et rajouter les d"tails
        self._inscriptions_df = self._inscriptions_df.explode("cours_json")

        df_merged = self._inscriptions_df.merge(
            self._cours_df, left_on="cours_json", right_on="mnemonique", how="left"
        ).drop(columns="cours_json")
        df_full = df_merged.merge(
            self._notes_df, on=["matricule", "mnemonique"], how="left"
        ).astype({"id": "Int64", "note": "Int64", "credit": "Int64"})

        # Construire un bulletin par étudiant
        self._bulletin_dataframe = (
            df_full.groupby(
                ["matricule", "nom", "prenom", "annee_etude"], as_index=False
            )
            .apply(
                lambda group: pd.Series(
                    {
                        "ects_total_inscrits": self._ects_total_inscrits(group),
                        "ects_obtenus": self._ects_obtenus(group),
                        "moyenne_ponderee": self._moyenne_ponderee(group),
                        "reussite": self._reussite(group),
                        "details": self._details(group),
                    }
                ),
                include_groups=False,
            )
            .rename(columns={"annee_etude": "annee"})
        )

    def load(self):
        self._bulletin_dataframe.to_csv(settings.BULLETIN_OUTPUT_PATH, index=False)
