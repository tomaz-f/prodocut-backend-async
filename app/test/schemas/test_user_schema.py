from app.schemas.user import User, TokenData
import pytest
from datetime import datetime


def test_user_schema():
    user = User(username='Felipe', password='nsi#1234')
    assert user.dict() == {
        'username': 'Felipe',
        'password': 'nsi#1234'
    }


def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='João#', password='nsi#1234')


def test_token_date():
    expires_at = datetime.now()
    token_data = TokenData(
        access_token='token qualquer',
        expires_at=expires_at
    )

    assert token_data.dict() == {
        'access_token': 'token qualquer',
        'expires_at': expires_at
    }
