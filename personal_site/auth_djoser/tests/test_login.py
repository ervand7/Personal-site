from django.contrib.auth.models import User
from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.authtoken.models import Token


@mark.django_db
def test_success(session_unauthorized, user_json):
    client = session_unauthorized
    json = user_json

    url = reverse('user-list')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    url = reverse('login')
    json.pop('email')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['auth_token']

    token = Token.objects.first()
    assert token.key == resp.data['auth_token']

    user = User.objects.first()
    assert user
    assert user.username == json['username']


@mark.django_db
def test_failed(session_unauthorized, user_json):
    client = session_unauthorized
    json = user_json
    json.pop('email')

    url = reverse('login')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert resp.content == \
           b'{"non_field_errors":["Unable to log in with provided credentials."]}'

    token = Token.objects.first()
    assert not token
