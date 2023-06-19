from wishlist.models import Wish, WishList
from api.serializers import WishSerializer

from .response import ERROR, SUCCESS
from .wishlist_services import wishlist_exists


def wish_exists(wish_id: str) -> dict:
    """Провееряет существует ли желание"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    if wish_id is None:
        error['message'] = 'Не передан параметр wish_id.'
        return error
    try:
        wish = Wish.objects.filter(pk=wish_id)
        if not wish.exists():
            error['message'] = f'Желания с wish_id={wish_id} не существует.'
            return error
        else:
            return success
    except ValueError:
        error['message'] = 'Недопустимый формат параметра wish_id.'
        return error


def create_wish(
    wishlist_id: str,
    w_text: str,
    w_about: str,
    w_link: str
) -> dict:
    """Создание желания"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        # проверяем сущесвует ли список
        wl_exists = wishlist_exists(wishlist_id)
        if wl_exists['status'] == 'error':
            return wl_exists
        # проверяем переданы ли остальные параметры
        # (только текст, остальные не обязательны)
        if w_text is None or w_text == '':
            error['message'] = 'Не передан параметр text.'
            return error
        wish = Wish.objects.create(
            wishlist=WishList.objects.get(pk=wishlist_id),
            text=w_text,
            about=None if w_about == '' else w_about,
            link=None if w_link == '' else w_link,
        )
        success['wish'] = WishSerializer(wish).data
        return success
    except Exception:
        return error


def get_wish(wish_id: str) -> dict:
    """Чтение желания"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        w_exists = wish_exists(wish_id)
        if w_exists['status'] == 'error':
            return w_exists
        wish = Wish.objects.get(pk=wish_id)
        success['wish'] = WishSerializer(wish).data
        return success
    except Exception:
        return error


def delete_wish(wish_id: str) -> dict:
    """Удление желания"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        w_exists = wish_exists(wish_id)
        if w_exists['status'] == 'error':
            return w_exists
        Wish.objects.filter(pk=wish_id).delete()
        return success
    except Exception:
        return error


def book_wish(wish_id: str) -> dict:
    """Бронирование желания другими пользователями"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        w_exists = wish_exists(wish_id)
        if w_exists['status'] == 'error':
            return w_exists
        w = Wish.objects.get(pk=wish_id)
        w.is_busy = True
        w.save()
        return success
    except Exception:
        return error


def unbook_wish(wish_id: str) -> dict:
    """Отмена бронирования желания другими пользователями"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    try:
        w_exists = wish_exists(wish_id)
        if w_exists['status'] == 'error':
            return w_exists
        w = Wish.objects.get(pk=wish_id)
        w.is_busy = False
        w.save()
        return success
    except Exception:
        return error
