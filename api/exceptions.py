from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    NotAuthenticated,
    PermissionDenied,
    ParseError,
    AuthenticationFailed
)
from rest_framework.response import Response

from .services.response import ERROR


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    error = ERROR.copy()
    if isinstance(exc, NotAuthenticated):
        error['message'] = 'Вы не авторизованы.'
        response = Response(error, status=401)
    elif isinstance(exc, PermissionDenied):
        print(exc)
        error['message'] = 'У вас недостаточно прав.'
        response = Response(error, status=403)
    elif isinstance(exc, ParseError):
        error['message'] = 'Ошибка парсинга json.'
        response = Response(error, status=400)
    elif isinstance(exc, AuthenticationFailed):
        error['message'] = 'Ошибка авторизации.'
        response = Response(error, status=401)

    return response
