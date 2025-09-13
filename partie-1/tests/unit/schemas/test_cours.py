import pytest
from pydantic import ValidationError

from tests.factories.schemas import CoursOutSchemaFactory


def test_cours_schema__mnemonique_string_format__success():
    cours_schema = CoursOutSchemaFactory.build(mnemonique='MTH001')
    assert cours_schema.mnemonique == 'MTH001'

def test_cours_schema__mnemonique_string_invalid__raises_validation_error():
    with pytest.raises(ValidationError, match='[type=string_pattern_mismatch, input_value="some string", input_type=str]'):
        CoursOutSchemaFactory.build(mnemonique="some string")