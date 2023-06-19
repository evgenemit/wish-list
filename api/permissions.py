from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Провероверяет является ли пользователь владельцем"""

    def has_permission(self, request, view):

        user_id = request.GET.get('user_id', None)
        if not user_id:
            user_id = request.data.get('user_id', None)
        return user_id == str(request.user.pk)
