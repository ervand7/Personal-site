from django.conf import settings
from django.urls import include, path

urlpatterns = [
    # http://127.0.0.1:8000/api/v1/session-auth/login/
    # http://127.0.0.1:8000/api/v1/session-auth/logout/
    path(f'{settings.API_V1_BASE_PREFIX}/session-auth/', include('rest_framework.urls')),
]
