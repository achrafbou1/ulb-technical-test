from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory

from models.inscription import Inscription


class InscriptionModelFactory(SQLAlchemyFactory[Inscription]):
    pass