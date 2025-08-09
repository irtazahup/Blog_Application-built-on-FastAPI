from fastapi import APIRouter,Depends,status,HTTPException
import oauth
import schemas
from typing import List
from database import get_db
import models
from sqlalchemy.orm import Session
from repository import blog 

router = APIRouter(
    prefix='/blogs',  # Prefix for all routes in this router
    tags=['Blogs']  
    # Tag for the router
)

@router.get('', status_code=status.HTTP_200_OK, response_model=list[schemas.AllBlogs])
def get_all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.get('/user', status_code=status.HTTP_200_OK, response_model=list[schemas.AllBlogs])
def get_user_blogs(db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.get_user_blog(db, get_current_user.id)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.AllBlogs)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.create_blog(request, db, get_current_user.id)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.AllBlogs)
def get_blog(id: int, db: Session = Depends(get_db)):
    return blog.get_blog(id, db)

@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.AllBlogs)
def get_user_blog(id: int, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.get_user_id_blog(db, get_current_user.id,id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.AllBlogs)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog .update_blog(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth.get_current_user)):
    return blog.delete_blog(id, db)

