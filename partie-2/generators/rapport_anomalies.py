import pandas as pd

from generators.base import BaseGenerator
from generators.bulletin import BulletinGenerator
from settings import settings


class RapportAnomaliesGenerator(BaseGenerator):
    _cours_df: pd.DataFrame
    _inscriptions_df: pd.DataFrame
    _notes_df: pd.DataFrame

    _rapport_anomalies: pd.DataFrame

    def __init__(self, bulletin_generator: BulletinGenerator):
        self.bulletin_generator = bulletin_generator

    def _add_details(self) -> pd.DataFrame:
        self._rapport_anomalies = self._rapport_anomalies.merge(
            self._cours_df, on="mnemonique", how="left"
        ).astype({"annee_etude": "Int64", "credit_x": "Int64"})

        self._rapport_anomalies = self._rapport_anomalies[
            [
                "type",
                "matricule",
                "annee_etude",
                "mnemonique",
                "intitule_y",
                "titulaire_y",
                "credit_y",
                "note",
            ]
        ]
        self._rapport_anomalies = self._rapport_anomalies.rename(
            columns={
                "credit_y": "credit",
                "annee_etude": "annee",
                "titulaire_y": "titulaire",
                "intitule_y": "intitule",
            }
        )

    def extract(self):
        self._cours_df = self.bulletin_generator._cours_df
        self._inscriptions_df = self.bulletin_generator._inscriptions_df
        self._notes_df = self.bulletin_generator._notes_df

    def transform(self):
        merged_notes = pd.merge(
            self._notes_df,
            self._inscriptions_df,
            left_on=["matricule", "mnemonique"],
            right_on=["matricule", "cours_json"],
            how="left",
            indicator=True,
        )

        # NOTE SANS INSCRIPTION
        note_sans_inscription = merged_notes[
            merged_notes["_merge"] == "left_only"
        ].copy()
        note_sans_inscription["type"] = "NOTE_SANS_INSCRIPTION"

        # COURS INCONNU
        cours_connu = set(self._cours_df["mnemonique"])
        self._inscriptions_df["cours_connu"] = self._inscriptions_df["cours_json"].isin(
            cours_connu
        )
        cours_inconnu = self._inscriptions_df[
            ~self._inscriptions_df["cours_connu"]
        ].copy()
        cours_inconnu["type"] = "COURS_INCONNU"

        # INSCRIPTION SANS COURS
        inscription_sans_cours = self._inscriptions_df[
            self._inscriptions_df["cours_json"].apply(lambda x: not x)
        ].copy()
        inscription_sans_cours["type"] = "INSCRIPTION_SANS_COURS"

        # DUPLICATA NOTE
        duplicata_note = self._notes_df.groupby(["matricule", "mnemonique"]).filter(
            lambda g: len(g) > 1
        )
        duplicata_note["anomaly_type"] = "DUPLICATA_NOTE"

        # NOTE SANS CREDIT
        merged_notes = pd.merge(
            self._notes_df,
            self._cours_df,
            on="mnemonique",
            how="left",
            indicator=True,
        )
        note_sans_credit = merged_notes[
            (merged_notes["credit"].isna()) | (merged_notes["credit"] <= 0)
        ].copy()
        note_sans_credit["type"] = "NOTE_SANS_CREDIT"

        # Combine all anomalies
        self._rapport_anomalies = pd.concat(
            [
                note_sans_inscription,
                cours_inconnu,
                inscription_sans_cours,
                duplicata_note,
                note_sans_credit,
            ],
            ignore_index=True,
        )

        self._add_details()

    def load(self):
        self._rapport_anomalies.to_json(
            settings.RAPPORT_ANOMALIES_OUTPUT_PATH, orient="records", indent=4
        )
