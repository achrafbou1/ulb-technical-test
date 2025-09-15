from fastapi import FastAPI
from controllers import cours, inscription, note
from settings import settings

description = """
## Cours
* Vous pouvez avoir la liste de tous les cours

## Inscriptions
* Vous pouvez avoir la liste de toutes les inscriptions

## Notes
* Vous pouvez avoir la liste de toutes les notes
* Vous pouvez avoir une note par mnemonique
"""

app = FastAPI(
    title="ulb-technical-test",
    description=description,
    summary="Cette API permet d'intéragir avec la base de données universite_demo.",
    version=str(settings.API_VERSION),
)

VERSION_STRING = f"/v{settings.API_VERSION}"

app.include_router(cours.router, prefix=VERSION_STRING)
app.include_router(inscription.router, prefix=VERSION_STRING)
app.include_router(note.router, prefix=VERSION_STRING)


@app.get("/")
async def healthcheck():
    return {"message": "API is running!"}
