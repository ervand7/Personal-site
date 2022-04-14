from random import randint

import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status

from core.models import Feedback


@pytest.fixture()
def feedback_json() -> dict:
    json = {
        "description": Faker('en').text(randint(50, 100)),
        "category": "Job",
        "content": Faker('en').text(randint(500, 1000)),
        "age_confirmation": True
    }
    return json


@pytest.fixture()
def create_feedback(feedback_json, create_token, create_user,
                    session_authorized) -> Feedback:
    json = feedback_json
    token = create_token(user=create_user())
    client = session_authorized(token=token)
    url = reverse('feedback-list')

    resp = client.post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    feedback = Feedback.objects.first()
    return feedback
