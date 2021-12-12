from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.dependancies import get_db
from sqlalchemy.orm import Session
from app.domain.exceptions import EntityNotFoundError, BadPasswordError
from app.domain.auth import authenticate
from app.api.models.login_response import LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> LoginResponse:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """
    try:
        return authenticate(email=form_data.username, password=form_data.password, db=db)
    except EntityNotFoundError or BadPasswordError:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
