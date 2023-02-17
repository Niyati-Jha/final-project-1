# from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
# from sqlalchemy.orm import Session
# from typing import Optional, List
# from .. import models, schemas # we have to travel up two directories to find these hence the ..
# from ..database import get_db

# router = APIRouter(
#     prefix="/sqlalchemy" , #"/sqlalchemy" + "/{id}"
#     tags=['sqlalchemyORM']
# )







# ############# Using the ORM models ##############

# @router.get("/", response_model= List[schemas.PostResponse]) # a list of pydantic models is sent
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts) #this actually returns the SQL statement that is abstracted from the user """not anymore tho"""
#     return  posts

 
# @router.post("/",status_code=status.HTTP_201_CREATED, response_model= schemas.PostResponse)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):   #HERE SCHEMA IS CREATEPOST
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post #the data has been removed and it is automatically serialized with the help of FASTAPI



# @router.get("/{id}")
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     print(post)
#     if not post:
#        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=  f"the post with id {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#     # print(post)
#     return post       #the data has been removed and it is automatically serialized with the help of FASTAPI



# @router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     if post_query.first() == None: #this first method executes the query
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"the id:{id} doesn't exist")
#     post_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)     



# @router.put("/{id}", response_model= schemas.PostResponse)
# def update_post(id: int, post: schemas.PostCreate,db: Session = Depends(get_db)): #HERE SCHEMA IS CREATEPOST
    
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     posts = post_query.first()
#     if posts == None:
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     post_query.update(post.dict(),synchronize_session=False)
#     db.commit()
#     return post_query.first() #the data has been removed and it is automatically serialized with the help of FASTAPI    
