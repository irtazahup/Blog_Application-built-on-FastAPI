from fastapi import status,HTTPException
import models
from sqlalchemy.orm import Session


def get_all(db: Session):
    
    blogs = db.query(models.Blog).all()
    return blogs

def get_user_blog(db: Session, user_id: int):
    blogs = db.query(models.Blog).filter(models.Blog.user_id == user_id).all()
    return blogs

def create_blog(request, db: Session,user_id: int):
    
    new_blog = models.Blog(
        title=request.title, 
        body=request.body,
        published=request.published,
        user_id=user_id  # You should replace this with actual user authentication
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

def get_user_id_blog(db:Session,user_id:int,blog_id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id, models.Blog.user_id == user_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found for current user")
    return blog

def update_blog(id: int, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.update({
        'title': request.title,
        'body': request.body,
        'published': request.published
    })
    db.commit()
    return blog.first()


def delete_blog(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog deleted successfully"}
