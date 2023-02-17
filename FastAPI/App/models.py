# When we create a tables using ORM we have to create tables using python 
# importing Base class from database.py

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Sequence
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship





class SensorDetail(Base):
    __tablename__ = "sensor_details"
    

    Sensor_ID = Column(Integer, primary_key=True, unique=True)
    Sensor_Name = Column(String, nullable=False)
    Sensor_Type = Column(String, nullable=False)
    Location = Column(String, nullable=False)

    sensor_data = relationship("SensorData", back_populates="sensor_detail")


class SensorData(Base):
    __tablename__ = "sensor_data"


    ID = Column(Integer,Sequence('my_table_id_seq'), primary_key=True, unique=True)
    Sensor_ID = Column(Integer, ForeignKey('sensor_details.Sensor_ID'))
    Sensor_Data = Column(String, nullable=False)
    Timestamp = Column(TIMESTAMP(timezone=True), nullable = False, server_default=text('now()'))

    sensor_detail = relationship("SensorDetail", back_populates="sensor_data")