from django.urls import reverse
from pytest import mark
from rest_framework import status


@mark.django_db
def test_success(create_user, create_token, session_authorized):
    token = create_token(user=create_user())
    session = session_authorized(token=token)
    url = reverse('logout')

    resp = session.post(url)
    assert resp.status_code == status.HTTP_204_NO_CONTENT


@mark.django_db
def test_failed(session_authorized):
    session = session_authorized(token='Hello')
    url = reverse('logout')

    resp = session.post(url)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
