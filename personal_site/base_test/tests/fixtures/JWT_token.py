import pytest
from django.urls import reverse
from mimesis import Person
from rest_framework import status


@pytest.fixture()
def get_jwt_token(request, session_unauthorized) -> dict:
    client = session_unauthorized

    json = {
        "email": Person('it').email(),
        "username": Person('it').username(),
        "password": Person('it').password()
    }
    url = reverse('user-list')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    json.pop('email')
    url = reverse('token_obtain_pair')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['refresh']
    assert resp.data['access']
    return resp.data
