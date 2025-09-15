from sqlalchemy import Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from db import Base
from models.cours import Cours


class Note(Base):
    __tablename__ = "liste_notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    matricule: Mapped[str] = mapped_column(Text, nullable=False)
    mnemonique: Mapped[str] = mapped_column(Text, ForeignKey(Cours.mnemonique))
    note: Mapped[int] = mapped_column(Integer, nullable=False)
