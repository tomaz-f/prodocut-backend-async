from app.schemas.user import User
import pytest


def test_user_schema():
    user = User(username='Felipe', password='nsi#1234')
    assert user.dict() == {
        'username': 'Felipe',
        'password': 'nsi#1234'
    }


def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='João#', password='nsi#1234')
