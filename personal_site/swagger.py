# https://habr.com/ru/company/otus/blog/583220/
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

swagger_schema = get_schema_view(
    openapi.Info(
        title="Ervand Agadzhanyan personal site API",
        default_version='v1',
        contact=openapi.Contact(email="ervand7@mail.ru"),
    ),
    patterns=[
        path('', include('core.urls')),
        path('', include('auth_djoser.urls')),
        path('', include('auth_JWT.urls')),
    ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_template_view = lambda: TemplateView.as_view(
    template_name='swaggerui.html',
    extra_context={'schema_url': 'openapi-schema'}
)
