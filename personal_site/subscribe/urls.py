from django.urls import path

from .views import SubscribeView, SuccessView, UnsubscribeView

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
    path('subscribe/success/', SuccessView.as_view(), name="success"),
]
