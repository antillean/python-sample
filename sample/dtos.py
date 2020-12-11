class UserDTO:
    def __init__(self, *, uid=None, name, email):
        self.uid = uid
        self.name = name
        self.email = email

    @staticmethod
    def from_model(user_model):
        assert user_model

        return UserDTO(uid=user_model.uid, name=user_model.username, email=user_model.email)

    def to_dict(self):
        return {"uid": self.uid, "name": self.name, "email": self.email}
