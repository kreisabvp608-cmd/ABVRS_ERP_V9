from sqlalchemy.orm import Session

from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from app.repositories.user_repository import get_user_by_username


def login(db: Session, username: str, password: str):

    user = get_user_by_username(db, username)

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role,
    }