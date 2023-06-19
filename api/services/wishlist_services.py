from user.models import CustomUser
from wishlist.models import WishList
from api.serializers import WishListSerializer, WishSerializer

from .response import ERROR, SUCCESS
from .user_services import user_exists


def wishlist_exists(wishlist_id: str) -> dict:
    """Проверяет существует ли список желаний"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    if wishlist_id is None:
        error['message'] = 'Не передан параметр wishlist_id.'
        return error
    try:
        if WishList.objects.filter(pk=wishlist_id).exists():
            return success
        error['message'] = f'Списка желаний с wishlist_id={wishlist_id} не существует.'
        return error
    except ValueError as e:
        error['message'] = 'Недопустимый формат параметра wishlist_id.'
        return error


def create_wishlist(user_id: str) -> dict:
    """Создает список желаний пользователя"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        # проверяем существует ли пользователь
        u_exists = user_exists(user_id)
        if u_exists['status'] == 'error':
            return u_exists
        # проверяем существует ли список
        if WishList.objects.filter(user__pk=user_id).exists():
            error['message'] = f'Список желаний пользователя c used_id={user_id} уже существует.'
            return error
        wishlist = WishList.objects.create(user=CustomUser.objects.get(pk=user_id))
        success['wishlist'] = WishListSerializer(wishlist).data
        return success
    except Exception as e:
        return error


def get_whislist(user_id: str) -> dict:
    """Возвращает информацию о списке желаний пользователя"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        u_exists = user_exists(user_id)
        if u_exists['status'] == 'error':
            return u_exists
        # проверяем существует ли список
        wishlist = WishList.objects.filter(user__pk=user_id)
        if not wishlist.exists():
            error['message'] = f'Список желаний пользователя c used_id={user_id} не существует.'
            return error
        wishlist = wishlist.first()
        success['wishlist'] = WishListSerializer(wishlist).data
        success['wishlist']['wishes'] = []
        for wish in wishlist.wishes.all().order_by('-pk'):
            success['wishlist']['wishes'].append(WishSerializer(wish).data)
        return success
    except Exception as e:
        return error


def delete_wishlist(user_id: str):
    """Удаляет список желаний"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        u_exists = user_exists(user_id)
        if u_exists['status'] == 'error':
            return u_exists
        WishList.objects.filter(user__pk=user_id).delete()
        return success
    except Exception as e:
        return error
