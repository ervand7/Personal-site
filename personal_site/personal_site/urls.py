import debug_toolbar
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import page_not_found
from personal_site import settings
from swagger import swagger_schema, swagger_template_view

swagger_urlpatterns = [
    path('swagger-ui/', swagger_template_view(), name='swagger-ui'),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        swagger_schema.without_ui(cache_timeout=0), name='schema-json'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('auth_JWT.urls')),
    path('', include('auth_session.urls')),
    path('', include('auth_djoser.urls')),
    path('', include('core.urls')),
    path('', include('subscribe.urls')),
    path('', include('summary.urls')),
] + swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
