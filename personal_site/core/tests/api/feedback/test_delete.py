from django.contrib.auth.models import User
from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.authtoken.models import Token

from core.models import Feedback


@mark.django_db
def test_success(create_feedback, session_authorized):
    feedback = create_feedback
    token = Token.objects.first()
    client = session_authorized(token=token)

    url = reverse('feedback-list') + f'{feedback.id}/'
    resp = client.delete(url)
    assert resp.status_code == status.HTTP_204_NO_CONTENT

    feedback = Feedback.objects.first()
    assert not feedback


@mark.django_db
def test_403(create_feedback, create_token, session_authorized):
    feedback = create_feedback
    url = reverse('feedback-list') + f'{feedback.id}/'

    other_user = User.objects.create()
    token = create_token(user=other_user)
    client = session_authorized(token=token)
    resp = client.delete(url)
    assert resp.status_code == status.HTTP_403_FORBIDDEN

    feedback = Feedback.objects.first()
    assert feedback


@mark.django_db
def test_401(create_feedback, session_unauthorized):
    feedback = create_feedback
    url = reverse('feedback-list') + f'{feedback.id}/'

    resp = session_unauthorized.delete(url)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    feedback = Feedback.objects.first()
    assert feedback
