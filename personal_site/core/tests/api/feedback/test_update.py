from random import choice

from django.contrib.auth.models import User
from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.authtoken.models import Token

from core.models import Feedback


@mark.django_db
def test_success(create_feedback, session_authorized):
    feedback = create_feedback
    old_description = feedback.description
    token = Token.objects.first()
    client = session_authorized(token=token)

    url = reverse('feedback-list') + f'{feedback.id}/'
    new_description = 'Hello'
    json = feedback.as_dict
    json['description'] = new_description

    update_method = choice([client.put, client.patch])
    resp = update_method(url, json)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['description'] == new_description
    assert old_description != new_description


@mark.django_db
def test_403(create_feedback, create_token, session_authorized):
    feedback = create_feedback
    old_description = feedback.description

    url = reverse('feedback-list') + f'{feedback.id}/'
    new_description = 'Hello'
    json = feedback.as_dict
    json['description'] = new_description

    other_user = User.objects.create()
    token = create_token(user=other_user)
    client = session_authorized(token=token)
    update_method = choice([client.put, client.patch])
    resp = update_method(url, json)
    assert resp.status_code == status.HTTP_403_FORBIDDEN

    feedback = Feedback.objects.first()
    assert feedback.description == old_description


@mark.django_db
def test_401(create_feedback, session_unauthorized):
    feedback = create_feedback
    client = session_unauthorized
    url = reverse('feedback-list') + f'{feedback.id}/'

    update_method = choice([client.put, client.patch])
    resp = update_method(url, feedback.as_dict)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
