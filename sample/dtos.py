from __future__ import annotations

from typing import Dict, Optional, Any

from sample.models import UserModel


class UserDTO:
    def __init__(self, *, uid: Optional[int] = None, name: str, email: str, first_name: str,
                 surname: str) -> None:
        self.uid: Optional[int] = uid
        self.name: str = name
        self.email: str = email
        self.first_name: str = first_name
        self.surname: str = surname

    @staticmethod
    def from_model(user_model: UserModel) -> UserDTO:
        assert user_model

        return UserDTO(uid=user_model.uid,
                       name=user_model.username,
                       email=user_model.email,
                       first_name=user_model.first_name,
                       surname=user_model.surname)

    @staticmethod
    def from_request(request: Any) -> UserDTO:
        assert request

        return UserDTO(name=request['username'],
                       email=request['email'],
                       first_name=request['first_name'],
                       surname=request['surname'])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            "first_name": self.first_name,
            "surname": self.surname
        }
