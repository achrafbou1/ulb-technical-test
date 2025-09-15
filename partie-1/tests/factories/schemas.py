from polyfactory.factories.pydantic_factory import ModelFactory

from schemas.cours import CoursResponse


class CoursOutSchemaFactory(ModelFactory[CoursResponse]):
    pass
