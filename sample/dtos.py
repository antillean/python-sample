from __future__ import annotations

from typing import Dict, Optional, Any

from sample.models import UserModel


class UserDTO:
    def __init__(self, *, uid: Optional[int] = None, name: str, email: str) -> None:
        self.uid: Optional[int] = uid
        self.name: str = name
        self.email: str = email

    @staticmethod
    def from_model(user_model: UserModel) -> UserDTO:
        assert user_model

        return UserDTO(uid=user_model.uid, name=user_model.username, email=user_model.email)

    def to_dict(self) -> Dict[str, Any]:
        return {"uid": self.uid, "name": self.name, "email": self.email}
