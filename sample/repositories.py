from typing import List, cast

from flask_sqlalchemy import SQLAlchemy

from sample import db
from sample.models import UserModel


class UserRepository:
    def __init__(self) -> None:
        self.db: SQLAlchemy = db

    @staticmethod
    def get_all_users() -> List[UserModel]:
        return cast(List[UserModel], UserModel.query.all())

    @staticmethod
    def get_user_by_name(name: str) -> UserModel:
        return cast(UserModel, UserModel.query.filter_by(username=name).first())

    @staticmethod
    def create_user(*, username: str, email: str) -> UserModel:
        user = UserModel(username=username, email=email)
        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def update_user(*, username: str, email: str) -> UserModel:
        user_model = UserRepository.get_user_by_name(username)
        user_model.email = email

        db.session.add(user_model)
        db.session.commit()

        return user_model
