# https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#first-steps-with-django
from subscribe.celery.config import app as celery_app

__all__ = ['celery_app']
