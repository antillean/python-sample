from flask_sqlalchemy import DefaultMeta

from sample import db

BaseModel: DefaultMeta = db.Model


class UserModel(BaseModel):  # type: ignore
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.Text, nullable=False, default="")
    surname = db.Column(db.Text, nullable=False, default="")

    def __repr__(self) -> str:
        return f'<User {self.uid}, {self.username}, {self.email}>'
