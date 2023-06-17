from django.urls import path

from .wishlist_api import WishlistAPIView
from .wish_api import WishAPIView, BookWishAPIView, UnbookWishAPIView
from .user_api import UserWishlistAPIView


urlpatterns = [
    path('wishlist/', WishlistAPIView.as_view()),
    path('wish/', WishAPIView.as_view()),
    path('wish/book/', BookWishAPIView.as_view()),
    path('wish/unbook/', UnbookWishAPIView.as_view()),
    path('user/', UserWishlistAPIView.as_view()),
]
