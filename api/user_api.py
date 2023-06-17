from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .wishlist_api import WishlistAPIView
from .base_api import CustomGenericAPIView


class UserWishlistAPIView(WishlistAPIView):
    """Чтение списка желаний пользователя"""

    permission_classes = [AllowAny]
    http_method_names = ['get']
