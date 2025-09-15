from sqlalchemy import Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Cours(Base):
    __tablename__ = "liste_cours"

    mnemonique: Mapped[str] = mapped_column(Text, primary_key=True)
    credit: Mapped[int] = mapped_column(Integer, nullable=False)
    intitule: Mapped[str] = mapped_column(Text, nullable=False)
    titulaire: Mapped[str] = mapped_column(Text, nullable=False)
