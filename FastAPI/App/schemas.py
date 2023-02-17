
from pydantic import BaseModel, EmailStr
from datetime import datetime
from datetime import date





class Write_Sensor(BaseModel):
    Sensor_ID: int
    Sensor_Name: str
    Sensor_Type: str
    Location: str
    class Config:
        orm_mode = True

class Write_Data(BaseModel):
    Sensor_ID: int
    Sensor_Data: str  
    Timestamp: datetime = datetime.now()
    



class Read_Sensor(BaseModel):
    ID: str
    Sensor_ID: int
    Sensor_Data: str
    Timestamp: datetime


# Used for email and password verification
class UserCreate(BaseModel):
    email: EmailStr
    password: str   














