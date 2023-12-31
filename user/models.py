from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомный пользователь"""

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username
