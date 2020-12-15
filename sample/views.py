from typing import Any, Dict

from flask import request

from sample import app
from sample.dtos import UserDTO
from sample.services import UserService


@app.route('/', methods=['GET'])
def hello_world() -> str:
    return 'Hello, World!'


@app.route('/users', methods=['GET'])
def get_list() -> Dict[str, Any]:
    result = [user_dto.to_dict() for user_dto in UserService.get_all_users()]
    return {"data": result}


@app.route('/users/<username>', methods=['GET'])
def get_user(username: str) -> Dict[str, Any]:
    return UserService.get_user_by_name(username).to_dict()


@app.route('/users', methods=['POST'])
def create_user() -> Dict[str, int]:
    request_body = request.json
    user_dto = UserDTO.from_request(request_body)

    uid = UserService.create_user(user_dto)
    return {"uid": uid}


@app.route('/users/<username>', methods=['PUT'])
def update_user(username: str) -> Dict[str, Any]:
    request_body = request.json
    user_dto = UserDTO.from_request(request_body)

    UserService.update_user(user_dto)
    return UserService.get_user_by_name(username).to_dict()
