from models import Farmland
from sqlalchemy.orm import Session


def get_farmland_list(db: Session):
    question_list = db.query(Farmland).order_by(Farmland.create_date.desc()).all()
    return question_list

