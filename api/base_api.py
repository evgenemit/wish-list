from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .services.response import ERROR
from .permissions import IsOwner


class CustomGenericAPIView(GenericAPIView):
    """Кастомный GenericAPIView"""

    permission_classes = [IsAdminUser | IsOwner]

    def http_method_not_allowed(self, request, *args, **kwargs):
        error = ERROR.copy()
        error['message'] = f'Метод {request.method} не разрешен.'
        return Response(error, status=405)
