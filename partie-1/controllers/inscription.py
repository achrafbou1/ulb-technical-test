from fastapi import APIRouter, Depends
from dependencies import get_db
from schemas.inscription import InscriptionOut
from services.inscription import InscriptionService

router = APIRouter(prefix="/inscription", tags=["inscription"])


@router.get("/", response_model=list[InscriptionOut])
async def get_inscriptions(db=Depends(get_db)):
    inscription_service = InscriptionService(db)
    return await inscription_service.get_all()