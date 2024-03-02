from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import update
from sqlalchemy.orm import Session
from blog import models, schemas
from ...database import get_db
from ...hashing import Hash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/", response_model=schemas.ShowUser)
def login(
    request: schemas.User,
    db: Session = Depends(get_db),
    
):
    hashing_password = Hash()
    get_user_data = (
        db.query(models.User).filter(models.User.email == request.email).first()
    )
    if not get_user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not found"
        )
    if not hashing_password.verify(str(get_user_data.password), request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password"
        )
    return get_user_data
