from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(
        'ws/wishlist/<str:wishlist_name>/',
        consumers.WishlistConsumer.as_asgi()
    ),
]
