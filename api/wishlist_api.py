from rest_framework.response import Response

from .serializers import WishListSerializer
from .base_api import CustomGenericAPIView
from .services import wishlist_services


class WishlistAPIView(CustomGenericAPIView):
    """Создание, удаление и чтение списка желаний"""

    http_method_names = ['get', 'post', 'delete']
    serializer_class = WishListSerializer

    def get(self, request):
        """Чтение списка"""
        user_id = request.GET.get('user_id', None)
        return Response(wishlist_services.get_whislist(user_id))

    def post(self, request):
        """Создание списка"""
        user_id = request.data.get('user_id', None)
        return Response(wishlist_services.create_wishlist(user_id))

    def delete(self, request):
        """Удаление списка"""
        user_id = request.data.get('user_id', None)
        return Response(wishlist_services.delete_wishlist(user_id))
