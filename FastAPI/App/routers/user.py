# from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
# from sqlalchemy.orm import Session
# from .. import models, schemas, utils # we have to travel up two directories to find these hence the ..
# from ..database import get_db


# router = APIRouter(
#     prefix="/users" ,  # this is a totally optional step, it justs makes things easier to read
#     tags=['users']
# )



# ######################### CREARING USER AUTHENTICATION USING NEW ORM MODEL #########################




# @router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut)  #app replaced by router 
# def Create_user(user : schemas.UserCreate, db: Session = Depends(get_db)):


#     hashed_password = utils.hash(user.password) #hashing the password
#     user.password = hashed_password #storing the hashed password back in the user.object


#     new_user = models.User(**user.dict()) #unpacking the User in the User model
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user




# #Retrieving the users based on their ID 
# @router.get("/{id}", response_model=schemas.UserOut) #app replaced by router 
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first() 
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")


#     return user      