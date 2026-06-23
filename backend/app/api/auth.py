from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

service = AuthService()

@router.post("/register")
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db)
):

    return service.register(
        db,
        payload
    )
    
@router.post("/login")
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):

    token = service.login(
        db,
        payload.email,
        payload.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token
    }