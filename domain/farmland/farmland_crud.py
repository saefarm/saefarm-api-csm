from datetime import datetime
from models import Farmland
from sqlalchemy.orm import Session
from domain.farmland import farmland_schema


def get_farmland_list(db: Session):
    question_list = db.query(Farmland).order_by(Farmland.create_date.desc()).all()
    return question_list


def create_farmland(db: Session, farmland_create: farmland_schema.FarmlandCreate):
    db_farmland = Farmland(
        farmland=farmland_create.farmland,
        latitude=farmland_create.latitude,
        longitude=farmland_create.longitude,
        weather_alias=farmland_create.weather_alias,
        soil_alias=farmland_create.soil_alias,
        exp_alias=farmland_create.exp_alias,
        farm_size=farmland_create.farm_size,
        is_foreign=farmland_create.is_foreign,
        create_date=datetime.now()
    )
    db.add(db_farmland)
    db.commit()


def read_farmland(db: Session, farmland: str):
    try:
        result = db.query(Farmland).filter(Farmland.farmland == farmland).all()
        return result[0]

    except IndexError:
        return False


def update_farmland(db: Session, farmland: str):
    try:
        result = db.query(Farmland).filter(Farmland.farmland == farmland).all()
        return result[0]

    except IndexError:
        return False


def delete_farmland(db: Session, db_farmland):
    db.delete(db_farmland)
    db.commit()

