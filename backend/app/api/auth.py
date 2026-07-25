from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    result = login(
        db,
        request.username,
        request.password,
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return result