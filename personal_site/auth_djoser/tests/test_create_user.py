from django.contrib.auth.models import User
from django.urls import reverse
from pytest import mark
from rest_framework import status


@mark.django_db
def test_success(session_unauthorized, user_json):
    client = session_unauthorized
    json = user_json

    user = User.objects.first()
    assert not user

    url = reverse('user-list')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    user = User.objects.first()
    assert user
    assert user.username == json['username']

    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert resp.content == b'{"username":["A user with that username already exists."]}'


@mark.django_db
def test_failed(session_unauthorized, user_json):
    client = session_unauthorized
    json = user_json
    json.pop('password')

    user = User.objects.first()
    assert not user

    url = reverse('user-list')
    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert resp.content == b'{"password":["This field is required."]}'

    user = User.objects.first()
    assert not user
