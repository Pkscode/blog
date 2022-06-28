from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List

# from blog.routers.oauth2 import get_current_user
from .. import Schemas, database, models # as we need to go two directories up so we used two dots here
from sqlalchemy.orm import Session
from ..repository import blog
from ..routers import oauth2

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

get_db = database.get_db

@router.get('/', response_model=List[Schemas.ShowBlog]) #copied from main.py (get all blogs section) and instead of app, router is used
def all(db : Session = Depends(get_db), current_user : Schemas.User = Depends(oauth2.get_current_user)):
    # blogs =db.query(models.Blog).all()
    # return blog.get_all()
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED) #import status from FastAPI
def create(request :Schemas.Blog, db: Session =Depends(get_db), current_user : Schemas.User = Depends(oauth2.get_current_user)):
    # new_blog =models.Blog(title=request.title, body=request.body, user_id = 1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db) 


#get blogs based on the IDs
@router.get('/{id}', status_code=200, response_model=Schemas.ShowBlog) # ShowBlog func is defined in Schemas.py
def show(id : int, db : Session = Depends(get_db), current_user : Schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # # lets say there is no blog at some ID
    # if not blog:
    #     # response.status_code=status.HTTP_404_NOT_FOUND #import Response from FastAPI
    #     # return {"detail": f"Blog with the ID {id} is not found"}
    #     # instead of above two lines , we can do it one line with HTTPException   
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the ID {id} is not found") 
    # return blog
    return blog.show(id, db)




# delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id : int, db: Session = Depends(get_db), current_user : Schemas.User = Depends(oauth2.get_current_user)):
#     blog= db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'Deleted Successfully'
      return blog.destroy(id, db)




#update a blog, also check if that id is available in the database
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id :int, request : Schemas.Blog, db: Session = Depends(get_db), current_user : Schemas.User = Depends(oauth2.get_current_user)):
    # blog= db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # blog.update(request)
    # db.commit()
    # return 'Updation Successfully'
    return blog.update(id, request, db)

