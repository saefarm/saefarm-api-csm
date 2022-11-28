import datetime

from pydantic import BaseModel, validator


class Farmland(BaseModel):
    id: int
    farmland: str
    latitude: float
    longitude: float
    weather_alias: str
    soil_alias: str
    exp_alias: str
    farm_size: int
    create_date: datetime.datetime
    is_foreign: bool

    class Config:
        orm_mode = True


class FarmlandCreate(BaseModel):
    farmland: str
    latitude: float
    longitude: float
    weather_alias: str
    soil_alias: str
    exp_alias: str
    farm_size: int
    create_date: datetime.datetime
    is_foreign: bool

    class Config:
        orm_mode = True


class FarmlandSummary(BaseModel):
    farmland: str
    latitude: float
    longitude: float
    farm_size: int
    create_date: datetime.datetime

    class Config:
        orm_mode = True


class FarmlandDelete(BaseModel):
    farmland: str

    class Config:
        orm_mode = True
