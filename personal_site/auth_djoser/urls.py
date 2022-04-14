from django.conf import settings
from django.urls import include, path

urlpatterns = [
    # authorization by djoser. See HTTP requests/djoser.http
    path(f'{settings.API_V1_BASE_PREFIX}/auth/', include('djoser.urls')),
    path(f'{settings.API_V1_BASE_PREFIX}/auth/', include('djoser.urls.authtoken')),
]
