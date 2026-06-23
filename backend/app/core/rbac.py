from fastapi import HTTPException
from fastapi import Depends

from app.core.dependencies import (
    get_current_user
)

def require_admin(
    user=Depends(
        get_current_user
    )
):

    if user["role"] != "ADMIN":

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return user