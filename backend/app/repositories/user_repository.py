from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def create(
        self,
        db: Session,
        name: str,
        email: str,
        password_hash: str = None
    ):

        user = User(
            name=name,
            email=email,
            password_hash=password_hash
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user

    def get_all(
        self,
        db: Session
    ):

        return db.query(User).all()
    
    def get_by_email(
        self,
        db,
        email
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )