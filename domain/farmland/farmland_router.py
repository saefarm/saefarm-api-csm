from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.farmland import farmland_schema, farmland_crud


router = APIRouter(
    prefix='/csm/farmland'
)


@router.get("/list", response_model=list[farmland_schema.Farmland])
def farmland_list(db: Session = Depends(get_db)):   # Dependency
    _farmland_list = farmland_crud.get_farmland_list(db)
    return _farmland_list
