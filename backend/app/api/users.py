from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate

from app.services.audit_service import AuditService
from app.core.dependencies import (
    get_current_user
)
from app.core.rbac import require_admin

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

repo = UserRepository()
audit_service = AuditService()


@router.post("")
async def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    print(payload)
    user = repo.create(
        db,
        payload.name,
        payload.email
    )

    await audit_service.log_event(
        "USER_CREATED",
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return user


@router.get("")
def get_users(
    db: Session = Depends(get_db)
):

    return repo.get_all(db)

@router.get("/profile")
def profile(
    user=Depends(
        get_current_user
    )
):

    return user

@router.get("/admin")
def admin_only(
    user=Depends(
        require_admin
    )
):

    return {
        "message":"Admin access granted"
    }