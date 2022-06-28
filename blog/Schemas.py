from pydantic import BaseModel
from typing import List, Union

class BlogBase(BaseModel) : #inserting basemodel to convert the textfields into Request Body
    title: str
    body: str

class Blog(BlogBase) :
    class Config() :
        orm_mode =True

class User(BaseModel) :
    name:str
    email:str
    password:str
    
class ShowUser(BaseModel) :
    name:str
    email:str
    # password:str
    blogs : List[Blog]

    class Config() :
        orm_mode =True

class ShowBlog(BaseModel) : #this function is moved here because compilation is done line by line 
    title: str
    body: str
    creator: ShowUser

    class Config() :
        orm_mode =True

class Login(BaseModel) :
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None #inplace of union, we need to write Optional as per tutorial 