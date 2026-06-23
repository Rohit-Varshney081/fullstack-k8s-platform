from app.core.security import (
    hash_password,
    verify_password
)

from app.core.jwt import (
    create_access_token
)

from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self):

        self.repo = UserRepository()

    def register(
        self,
        db,
        payload
    ):

        password_hash = hash_password(
            payload.password
        )

        return self.repo.create(
            db,
            payload.name,
            payload.email,
            password_hash
        )

    def login(
        self,
        db,
        email,
        password
    ):

        user = self.repo.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash
        ):
            return None

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role
            }
        )

        return token
    