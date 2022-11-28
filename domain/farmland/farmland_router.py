from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.farmland import farmland_schema, farmland_crud

router = APIRouter(
    prefix='/csm/farmland'
)


@router.get("/list", response_model=list[farmland_schema.FarmlandSummary])
def farmland_list(db: Session = Depends(get_db)):  # Dependency
    _farmland_list = farmland_crud.get_farmland_list(db)
    print(_farmland_list[0].farmland)
    return _farmland_list


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def farmland_create(_farmland_create: farmland_schema.FarmlandCreate,
                  db: Session = Depends(get_db)):  # Dependency
    farmland_crud.create_farmland(
        db,
        farmland_create=_farmland_create
    )


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def farmland_list(_farmland_delete: farmland_schema.FarmlandDelete,
                  db: Session = Depends(get_db)):  # Dependency
    db_farmland = farmland_crud.read_farmland(db, _farmland_delete.farmland)
    if not db_farmland:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    farmland_crud.delete_farmland(
        db,
        db_farmland
    )
