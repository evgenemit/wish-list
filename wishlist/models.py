from django.db import models


class Wish(models.Model):
    """Желание - элемент списка желаний"""

    text = models.CharField(max_length=100, verbose_name='Текст')
    about = models.TextField(null=True, blank=True, verbose_name='Описание')
    is_busy = models.BooleanField(default=False, verbose_name='Занято?')
    link = models.URLField(null=True, blank=True, verbose_name='Ссылка')
    wishlist = models.ForeignKey(
        'WishList',
        on_delete=models.CASCADE,
        related_name='wishes',
        verbose_name='Список желаний'
    )

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'

    def __str__(self) -> str:
        return self.text


class WishList(models.Model):
    """Список желаний"""

    user = models.OneToOneField(
        'user.CustomUser',
        on_delete=models.CASCADE,
        related_name='wishlist',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Список желаний'
        verbose_name_plural = 'Списки желаний'

    def __str__(self) -> str:
        return f'{self.user} wishlist'
