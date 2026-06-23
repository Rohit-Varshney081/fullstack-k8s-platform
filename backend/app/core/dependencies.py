from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer

from jose import jwt

from app.core.config import settings

security = HTTPBearer()

def get_current_user(
    credentials=Depends(security)
):

    try:

        payload = jwt.decode(
            credentials.credentials,
            settings.JWT_SECRET_KEY,
            algorithms=[
                settings.JWT_ALGORITHM
            ]
        )

        return payload

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )