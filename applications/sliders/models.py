from django.db import models

from ..core.models import Common, PathAndRename, Single


class SliderPreference(Single):
    """ Настройки блока слайдер """

    title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )

    content = models.TextField(
        verbose_name='Контент',
        help_text='Для того,чтобы выделить написать внутри тега <a></a>',
    )

    class Meta:
        verbose_name = 'настройки блока слайдер'
        verbose_name_plural = 'настройки блока слайдер'

    def __str__(self):
        return self.title


class Slider(Common):
    """ Слайдер """

    preference = models.ForeignKey(
        verbose_name='настройки',
        to=SliderPreference,
        on_delete=models.CASCADE,
        related_name='sliders',
    )

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('sliders/slider/image'),
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'слайдеры'
        verbose_name_plural = 'слайдеры'

    def __str__(self):
        return f'{self.id}'
