from sqlalchemy import Table, Integer, Column, Text
from sqlalchemy.orm import Mapped

from db import Base, metadata, engine

class Inscription(Base):
    __tablename__ = "liste_inscriptions"

    annee_etude: Mapped[int] = Column(Integer, primary_key=True)
    matricule: Mapped[str] = Column(Text, primary_key=True)
    cours_json: Mapped[str] = Column(Text, nullable=False)
    nom: Mapped[str] = Column(Text, nullable=False)
    prenom: Mapped[str] = Column(Text, nullable=False)