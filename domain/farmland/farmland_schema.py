import datetime

from pydantic import BaseModel


class Farmland(BaseModel):
    id: int
    farmland: str
    latitude: float
    longitude: float
    weather_alias: str
    soil_alias: str
    exp_alias: str
    farm_size: int
    is_foreign: bool
    create_data: datetime.datetime

    class Config:
        orm_mode = True
