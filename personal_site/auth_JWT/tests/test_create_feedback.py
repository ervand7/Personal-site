import jwt
from django.urls import reverse
from pytest import mark
from rest_framework import status

from core.models import Feedback


@mark.django_db
def test_success(get_jwt_token, session_jwt_authorized, feedback_json):
    json = feedback_json
    session = session_jwt_authorized(
        jwt_token=get_jwt_token["access"])
    url = reverse('feedback-list')

    resp = session.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    feedback = Feedback.objects.first()
    assert json.items() <= feedback.__dict__.items()


@mark.django_db
def test_invalid_token(session_jwt_authorized, feedback_json):
    json = feedback_json
    wrong_token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    session = session_jwt_authorized(
        jwt_token=wrong_token)
    url = reverse('feedback-list')

    resp = session.post(url, json)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
    assert resp.data['messages'][0]['message'] == 'Token is invalid or expired'
