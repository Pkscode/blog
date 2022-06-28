from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from .. import Schemas, database, models, hashing # as we need to go two directories up so we used two dots here
from sqlalchemy.orm import Session
from ..repository import user

# from ..hashing import Hash
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED,response_model=Schemas.ShowUser)
def create_user(request : Schemas.User, db: Session = Depends(get_db)):
    # # hashedPassword = pwd_cxt.hash(request.password)  #now imported via Hashing.py
    # # return request
    # new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password), id =1) #models.User(request) # models.User(name=request.name, email=request.email, password=request.password)
    # #instead of this-> hashing.Hash.bcrypt(request.password), we can directly call Hash.bcrypt(request.password) after writing one line : from hashing import Hash 
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create_user(request, db)

@router.get('/{id}', response_model = Schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    # user= db.query(models.user).filter(models.user.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    # return user
    user.get_user(id, db)