from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Inscription(Base):
    __tablename__ = "liste_inscriptions"

    annee_etude: Mapped[int] = mapped_column(Integer, primary_key=True)
    matricule: Mapped[str] = mapped_column(Text, primary_key=True)
    cours_json: Mapped[str] = mapped_column(Text, nullable=False)
    nom: Mapped[str] = mapped_column(Text, nullable=False)
    prenom: Mapped[str] = mapped_column(Text, nullable=False)
