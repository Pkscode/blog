
from http.client import HTTPException
from fastapi import APIRouter, Depends, status
from ..import Schemas, database, models
from sqlalchemy.orm import Session

from ..hashing import Hash

from ..routers import token

from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(
    tags=['Authentication']
)
@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    # generate a jwt token and return
    access_token = token.create_access_token(data={"sub": user.email}) #import token
    return {"access_token": access_token, "token_type": "bearer"}
    #copy pasted from documentation
