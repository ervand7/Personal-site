import pytest
from rest_framework.authtoken.models import Token


@pytest.fixture()
def create_token():
    def inner(**kwargs):
        return Token.objects.create(**kwargs)

    return inner
