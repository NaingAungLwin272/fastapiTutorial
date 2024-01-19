from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import update
from sqlalchemy.orm import Session
from blog import models, schemas
from ...database import get_db

router = APIRouter()


@router.post("/create", status_code=201)
def create_blog(
    request: schemas.BlogModel, db: Session = Depends(get_db)
) -> schemas.BlogModel:
    new_blog = models.Blog(title=request.title, description=request.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    get_blog_by_id = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not get_blog_by_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )
    return get_blog_by_id


@router.get("/blog_lists", response_model=List[schemas.ShowBlogModel])
def get_blog_list(db: Session = Depends(get_db)):
    blog_lists = db.query(models.Blog).all()
    return blog_lists


# With Returning updated data -------------
@router.put("/update/{blog_id}")
def update_blog(
    blog_id: int, request: schemas.BlogModel, db: Session = Depends(get_db)
):
    blog_data = get_blog(blog_id, db)
    if blog_data:
        update_query = (
            update(models.Blog)
            .where(models.Blog.id == blog_id)
            .values(title=request.title, description=request.description)
            .returning(models.Blog)
        )
        result = db.scalar(update_query)
        db.refresh(result)
        return {"data": result, "message": "Updated Successfully"}


@router.delete("/delete/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog_data = get_blog(blog_id, db)
    if blog_data:
        db.query(models.Blog).filter(models.Blog.id == blog_id).delete()
        db.commit()
        return {"data": "Blog deleted successfully"}
