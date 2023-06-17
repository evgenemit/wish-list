from user.models import CustomUser

from .response import ERROR, SUCCESS


def user_exists(user_id: str) -> dict:
    """Проверяет существует ли пользователь"""

    error = ERROR.copy()
    success = SUCCESS.copy()
    if user_id is None:
        error['message'] = 'Не передан параметр user_id.'
        return error
    try:
        if CustomUser.objects.filter(pk=user_id).exists():
            return success
        error['message'] = f'Пользователя с user_id={user_id} не существует.'
        return error
    except ValueError as e:
        error['message'] = 'Недопустимый формат параметра user_id.'
        return error
