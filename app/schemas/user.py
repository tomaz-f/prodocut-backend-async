from app.schemas.base import CustomBaseModel
from pydantic import validator
import re


class User(CustomBaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value
