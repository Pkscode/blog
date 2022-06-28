from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import Schemas, models, hashing
from sqlalchemy.orm import Session

def create_user(request : Schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password)) #models.User(request) # models.User(name=request.name, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id, db: Session):
    user= db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user