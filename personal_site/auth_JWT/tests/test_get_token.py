from django.urls import reverse
from pytest import mark
from rest_framework import status


@mark.django_db
def test_success(get_jwt_token):
    pass


@mark.django_db
def test_fail(session_unauthorized, user_json):
    client = session_unauthorized
    json = user_json
    json.pop('email')

    url = reverse('token_obtain_pair')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
