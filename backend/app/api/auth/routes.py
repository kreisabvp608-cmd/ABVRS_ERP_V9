from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import TokenResponse
from app.services.auth_service import login
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    result = login(
        db,
        form_data.username,
        form_data.password,
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return result


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "message": "Authentication Successful",
        "user": current_user,
    }