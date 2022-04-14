from django.urls import reverse
from pytest import mark
from rest_framework import status


@mark.django_db
def test_success(session_unauthorized, session_authorized,
                 create_token, create_user, feedback_json):
    json = feedback_json
    token = create_token(user=create_user())
    url = reverse('feedback-list')

    resp = session_authorized(token=token).post(url, json)
    assert resp.status_code == status.HTTP_201_CREATED

    url = reverse('feedback-list')
    resp = session_unauthorized.get(url)
    assert resp.status_code == status.HTTP_200_OK
    feedback = resp.data['results'][0]
    assert feedback

    retrieve_endpoint = f"{feedback['id']}/"
    resp = session_unauthorized.get(url + retrieve_endpoint)
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['description'] == json['description']
