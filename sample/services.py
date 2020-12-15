from typing import List, cast

from sample.dtos import UserDTO
from sample.repositories import UserRepository


class UserService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_all_users() -> List[UserDTO]:
        return [UserDTO.from_model(user_model) for user_model in UserRepository.get_all_users()]

    @staticmethod
    def get_user_by_name(name: str) -> UserDTO:
        assert name

        user_model = UserRepository.get_user_by_name(name)

        return UserDTO.from_model(user_model)

    @staticmethod
    def create_user(user_dto: UserDTO) -> int:
        assert user_dto
        user_model = UserRepository.create_user(username=user_dto.name, email=user_dto.email,
                                                first_name=user_dto.first_name, surname=user_dto.surname)

        return cast(int, user_model.uid)

    @staticmethod
    def update_user(user_dto: UserDTO) -> UserDTO:
        assert user_dto
        user_model = UserRepository.update_user(username=user_dto.name, email=user_dto.email,
                                                first_name=user_dto.first_name, surname=user_dto.surname)

        return UserDTO.from_model(user_model)
