from django.db import models

from ..core.models import PathAndRename, Single


class About(Single):
    """ о нас """

    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )

    content = models.TextField(
        verbose_name='Контент',
        help_text=
        'Для выделения первой буквы/слова использовать <span class="firstcharacter"></span>',
    )

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('about/about/image'),
    )

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
