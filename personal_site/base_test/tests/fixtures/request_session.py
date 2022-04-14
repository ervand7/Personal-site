import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def session_authorized(request):
    def inner(token):
        session = APIClient()
        session.credentials(HTTP_AUTHORIZATION="Token %s" % token)
        return session

    return inner


@pytest.fixture()
def session_jwt_authorized(request):
    def inner(jwt_token):
        session = APIClient()
        session.credentials(HTTP_AUTHORIZATION=f"Bearer {jwt_token}")
        return session

    return inner


@pytest.fixture()
def session_unauthorized(request):
    return APIClient()
