from pydantic import BaseModel
from typing import List, Optional

class ShowUser(BaseModel):
    
    name:str
    email:str
      # Use forward reference for ShowBlogs
    class Config:
        from_attributes=True
              

class Blog(BaseModel):
    title: str
    body: str
    published: bool = True
  
    class Config:
        from_attributes = True

class ShowBlogWithUser(BaseModel):
    name:str
    email:str
class ShowBlogs(BaseModel):
    
    title: str
    body: str
    published: bool = True
    creator:ShowBlogWithUser
    class Config:
        from_attributes = True
        
class AllBlogs(BaseModel):
    title: str
    body: str
    published: bool = True
    class Config:
        from_attributes = True
        
class User(BaseModel):
    name:str
    email:str
    password:str

    class Config:
        from_attributes=True


# class ShowUser(BaseModel):
#     name:str
#     email:str
    
#     class Config:
#         from_attributes=True
              
        
class UserLogin(BaseModel):
    email:str
    password:str

    class Config:
        from_attributes=True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    email:Optional[str] = None