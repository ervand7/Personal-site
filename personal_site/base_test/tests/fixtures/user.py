import pytest
from mimesis import Person
from model_bakery import baker


@pytest.fixture()
def create_user():
    def inner(**kwargs):
        return baker.make("User", **kwargs)

    return inner


@pytest.fixture()
def user_json() -> dict:
    json = {
        "email": Person('it').email(),
        "username": Person('it').username(),
        "password": Person('it').password()
    }

    return json
