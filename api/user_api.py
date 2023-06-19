from rest_framework.permissions import AllowAny

from .wishlist_api import WishlistAPIView


class UserWishlistAPIView(WishlistAPIView):
    """Чтение списка желаний пользователя"""

    permission_classes = [AllowAny]
    http_method_names = ['get']
