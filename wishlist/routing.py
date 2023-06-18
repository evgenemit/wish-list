from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/wishlist/<str:wishlist_name>/", consumers.WishlistConsumer.as_asgi()),
]