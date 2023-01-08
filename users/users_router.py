from fastapi import APIRouter
import uuid

router = APIRouter()
users = [
    {'seq': 1, 'uuid': uuid.uuid4(), 'id': 'jakesong5050', 'email': 'jakesong5050@gmail.com', 'password': '1234'},
    {'seq': 2, 'uuid': uuid.uuid4(), 'id': 'huntmori04x22', 'email': 'huntmori04x22@gmail.com', 'password': '1234'}
]


@router.get("/users/")
def read_users():
    return users


@router.get("/users/{user_seq}")
def read_one_user(user_seq: int):
    result = None
    for item in users:
        if item["seq"] == user_seq:
            result = item
    return result
