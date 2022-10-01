from django.urls import re_path

from .consumers import OrderConsumer

websocket_urlpatterns = [
    re_path('ws', OrderConsumer.as_asgi())
]
