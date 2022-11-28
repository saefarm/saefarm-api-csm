from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

from database import Base


class Farmland(Base):
    __tablename__ = "farmland"

    id = Column(Integer, primary_key=True)
    farmland = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    weather_alias = Column(String, nullable=False)
    soil_alias = Column(String, nullable=False)
    exp_alias = Column(String, nullable=False)
    farm_size = Column(Integer, nullable=False)      # Farm Size, Hectare
    is_foreign = Column(Boolean, nullable=False)
    create_date = Column(DateTime, nullable=False)


