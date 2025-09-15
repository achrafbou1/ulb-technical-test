import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_all__success(test_client: AsyncClient):
    """
    This tests that the cours endpoint returns the corresponding
    """
    response = await test_client.get("/v1/cours/")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["mnemonique"] == "MAT101"
    assert data[0]["credit"] == 5
    assert data[0]["intitule"] == "Analyse mathématique I"
    assert data[0]["titulaire"] == "Pr. Lefèvre"
