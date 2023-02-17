
from operator import index
from random import randrange
from typing import Optional, List
from urllib import response
from xml.dom.minidom import Identified
from fastapi import FastAPI, status, Response, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .routers import post, user,auth

# ORM
from . import models
from .database import engine,SessionLocal, get_db
    
models.Base.metadata.create_all(bind=engine)

# If the connection is not successful the loop keeps running
# and if it does it breaks out
# cursor creates the data in form of a dictionary... also check is the password the masterpassword

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user='postgres', password = '10p19fb1094', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was succesful")
        break
    except Exception as error:
        print("Connection to database failed")    
        print("Error:", error)
        time.sleep(2)







my_posts = [{"title1" : "this is the title one of the post1", "content1" : "this is the content of the post 1" ,"id" : 1},{"title2": "this is the title of the second post", "content2": "this is the content of the second post", "id" : 2}]

# A funtion to find posts
def find_post(id):
    for p in my_posts:
        if (p['id'] == id):
            return p






app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/write_data",status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.Write_Sensor, db: Session = Depends(get_db)):   #HERE SCHEMA IS CREATEPOST
    new_post = models.SensorDetail(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)   
    return new_post 

@app.get("/read_data", response_model= List[schemas.Read_Sensor]) # a list of pydantic models is sent
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.SensorData).all()
    # print(posts) #this actually returns the SQL statement that is abstracted from the user """not anymore tho"""
    return posts

@app.post("/write_sensors",status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.Write_Data, db: Session = Depends(get_db)):   #HERE SCHEMA IS CREATEPOST
    new_post = models.SensorData(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)   
    return new_post 

