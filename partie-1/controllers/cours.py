
from fastapi import APIRouter, Depends
from dependencies import get_db
from schemas.cours import CoursResponse
from services.cours import CoursService

router = APIRouter(prefix="/cours", tags=["cours"])


@router.get("/", response_model=list[CoursResponse])
async def get_cours(db=Depends(get_db)):
    cours_service = CoursService(db)
    return await cours_service.get_all()