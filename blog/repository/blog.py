from fastapi import Depends, status, Response, HTTPException
from typing import List
from .. import Schemas, models # as we need to go two directories up so we used two dots here
from sqlalchemy.orm import Session

def get_all(db : Session ):
    blogs =db.query(models.Blog).all()
    return blogs

def create(request :Schemas.Blog, db: Session):
    new_blog =models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id : int, db: Session = Depends):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully' 

def update(id: int, request : Schemas.Blog, db: Session = Depends):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return 'Updation Successfully'

def show(id : int, db : Session = Depends):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # lets say there is no blog at some ID
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND #import Response from FastAPI
        # return {"detail": f"Blog with the ID {id} is not found"}
        # instead of above two lines , we can do it one line with HTTPException   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the ID {id} is not found") 
    return blog