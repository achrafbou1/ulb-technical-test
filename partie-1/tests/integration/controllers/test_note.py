import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_get_by_id__success(test_client: AsyncClient):
    note_id = 1
    response = await test_client.get(f"/v1/note/{note_id}")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert data["matricule"] == "2023001"
    assert data["mnemonique"] == "MAT101"
    assert data["note"] == 14


@pytest.mark.anyio
async def test_get_by_id__notfound_id__returns_404(test_client: AsyncClient):
    note_id = 1254564
    response = await test_client.get(f"/v1/note/{note_id}")
    assert response.status_code == 404
