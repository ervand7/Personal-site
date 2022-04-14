from django.urls import reverse
from pytest import mark
from rest_framework import status

from core.models import Feedback


@mark.django_db
def test_success(create_token, create_user, session_authorized, feedback_json):
    json = feedback_json
    token = create_token(user=create_user())
    session = session_authorized(token=token)
    url = reverse('feedback-list')

    resp = session.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    feedback = Feedback.objects.first()
    assert json.items() <= feedback.__dict__.items()


@mark.django_db
def test_401(session_unauthorized, feedback_json):
    json = feedback_json
    url = reverse('feedback-list')

    resp = session_unauthorized.post(url, json)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    feedback = Feedback.objects.first()
    assert not feedback


@mark.django_db
def test_invalid_token(session_authorized, feedback_json):
    json = feedback_json
    session = session_authorized(token='Hello')
    url = reverse('feedback-list')

    resp = session.post(url, json)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.content == b'{"detail":"Invalid token."}'
