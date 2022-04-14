from django.apps import AppConfig


class BaseTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_test'
