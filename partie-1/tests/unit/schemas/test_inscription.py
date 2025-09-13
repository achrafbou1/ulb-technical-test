import pytest
from pydantic import ValidationError

from schemas.inscription import InscriptionOut
from tests.factories.models import InscriptionModelFactory

"""
    This ensures that a given inscription schema adheres
    to the defined validation rules. One of which being that cours_json should
    be returned as a list since it is stored as a string.

"""

def test_inscription_schema__list_in_string_passed__converted_to_list():

    inscription_model = InscriptionModelFactory.build(cours_json='["MTH001", "SSH258"]')

    inscription_out = InscriptionOut.model_validate(inscription_model)
    assert isinstance(inscription_out.cours_json, list)

def test_inscription_schema__non_convertible_string_passed__raises_error():

    inscription_model = InscriptionModelFactory.build(cours_json="some string")

    with pytest.raises(ValidationError, match='[type=value_error, input_value="some string", input_type=str]'):
        InscriptionOut.model_validate(inscription_model)




