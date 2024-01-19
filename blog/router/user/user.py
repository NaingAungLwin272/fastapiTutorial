from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import update
from sqlalchemy.orm import Session
from blog import models, schemas
from ...database import get_db
from ...hashing import hashing_password

router = APIRouter()


@router.post("/create_user", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=hashing_password(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user, "message": "User created successfully"}


@router.get("/{user_id}", response_model=schemas.ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_data = get_query_by_id(user_id, models.User, models.User.id, db)
    return user_data


def get_query_by_id(id: int, model, model_id, db: Session = Depends(get_db)):
    result = db.query(model).where(model_id == id).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Result not found"
        )
    return result
