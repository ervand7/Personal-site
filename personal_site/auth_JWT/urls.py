from django.conf import settings
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

urlpatterns = [
    path(f'{settings.API_V1_BASE_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{settings.API_V1_BASE_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{settings.API_V1_BASE_PREFIX}/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
