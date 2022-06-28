# import code
# from typing import List
# from fastapi import FastAPI, Depends, status, Response, HTTPException
# # from pydantic import BaseModel
# from . import Schemas
# # "." means importing from same directory

# # FOR DATA CONNECTION
# from .database import engine, get_db, SessionLocal #session local is not in use, you can remove it/ your wish
# from sqlalchemy.orm import Session

# from . import models, hashing
# # from . import crud

# from typing import List

# import blog





#Password Hashing
# from passlib.context import CryptContext
# Now,we will import via hashing.py

# app =FastAPI()

# class Blog(BaseModel) : #inserting basemodel to convert the textfields into Request Body
#     title: str
#     body: str
### Shifted to Schemas###



# migrating all the tables
# models.Base.metadata.create_all(engine)


# app.include_router(blog.router)
# app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try: 
#         yield db
#     finally:
#         db.close()
# shifted to database.py but make sure to import get_db here 



# @app.post('/blog', status_code=201)
# or
# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs']) #import status from FastAPI
# # def create(title, body):
# #     return {'title': title, 'body' : body}
# def create(request :Schemas.Blog, db: Session =Depends(get_db)):
#     # return db
#     new_blog =models.Blog(title=request.title, body=request.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog 
## Shifted to blog.py of routers page

#get blogs from database
# @app.get('/blog', response_model=List[Schemas.ShowBlog], tags=['blogs']) #we need to return list as we are returning collection of all blogs
# def all(db : Session = Depends(get_db)):
#     blogs =db.query(models.Blog).all()
#     return blogs
# shifted to blo.py of router folder

# #get blogs based on the IDs
# @app.get('/blog/{id}', status_code=200, response_model=Schemas.ShowBlog, tags=['blogs']) # ShowBlog func is defined in Schemas.py
# def show(id, response: Response, db : Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     # lets say there is no blog at some ID
#     if not blog:
#         # response.status_code=status.HTTP_404_NOT_FOUND #import Response from FastAPI
#         # return {"detail": f"Blog with the ID {id} is not found"}
#         # instead of above two lines , we can do it one line with HTTPException   
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the ID {id} is not found") 
#     return blog

# # delete a blog
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog= db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'Deleted Successfully'

# #update a blog, also check if that id is available in the database
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, request : Schemas.Blog, db: Session = Depends(get_db)):
#     blog= db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     blog.update(request)
#     db.commit()
#     return 'Updation Successfully'

# # pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") #taken from documentation, that bcrypt is forencryption
# # now imported via hashing.py

# @app.post('/user', status_code=status.HTTP_201_CREATED,response_model=Schemas.ShowUser, tags=['user'])
# def create_user(request : Schemas.User, db: Session = Depends(get_db)):
#     # hashedPassword = pwd_cxt.hash(request.password)  #now imported via Hashing.py
#     # return request
#     new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password), id =1) #models.User(request) # models.User(name=request.name, email=request.email, password=request.password)
#     #instead of this-> hashing.Hash.bcrypt(request.password), we can directly call Hash.bcrypt(request.password) after writing one line : from hashing import Hash 
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model = Schemas.ShowUser , tags=['user'])
# def get_user(id, db: Session = Depends(get_db)):
#     user= db.query(models.user).filter(models.user.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
#     return user

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app =FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)