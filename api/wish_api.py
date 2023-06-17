from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .base_api import CustomGenericAPIView
from .services import wish_services
from .services.response import ERROR, SUCCESS
from .serializers import WishSerializer


class WishAPIView(CustomGenericAPIView):
    """Создание, удаление и чтение желания"""

    http_method_names = ['get', 'post', 'delete']
    serializer_class = WishSerializer

    def get(selg, request):
        """Чтение желания"""
        wish_id = request.GET.get('wish_id', None)
        return Response(wish_services.get_wish(wish_id))

    def post(self, request):
        """Создание желания"""
        wishlist_id = request.data.get('wishlist_id', None)
        w_text = request.data.get('text', None)
        w_about = request.data.get('about', None)
        w_link = request.data.get('link', None)
        return Response(wish_services.create_wish(wishlist_id, w_text, w_about, w_link))

    def delete(self, request):
        """Удаляет желание"""
        wish_id = request.data.get('wish_id', None)
        return Response(wish_services.delete_wish(wish_id))


class BookWishAPIView(CustomGenericAPIView):
    """Бронирование желаний другими пользователями"""

    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        """Бронирование"""
        wish_id = request.data.get('wish_id', None)
        return Response(wish_services.book_wish(wish_id))


class UnbookWishAPIView(CustomGenericAPIView):
    """Отмена бронирования желаний другими пользователями"""

    permission_classes = [AllowAny]
    http_method_names = ['post']

    def post(self, request):
        """Отмена бронирования"""
        wish_id = request.data.get('wish_id', None)
        return Response(wish_services.unbook_wish(wish_id))
