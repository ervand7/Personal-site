import jwt
from django.urls import reverse
from pytest import mark
from rest_framework import status


@mark.django_db
def test_success(get_jwt_token, session_jwt_authorized):
    url = reverse('token_verify')
    access_token = get_jwt_token['access']
    client = session_jwt_authorized(jwt_token=get_jwt_token["access"])

    resp = client.post(url, {"token": access_token})
    assert resp.status_code == status.HTTP_200_OK
    assert not resp.data


@mark.django_db
def test_fail(get_jwt_token, session_jwt_authorized):
    url = reverse('token_verify')
    wrong_refresh_token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    client = session_jwt_authorized(jwt_token=get_jwt_token["access"])

    resp = client.post(url, {"token": wrong_refresh_token})
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data['detail'] == 'Token is invalid or expired'
