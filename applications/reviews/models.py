from django.db import models

from ..core.models import Common


class Review(Common):
    """  Отзыв """

    title = models.CharField(
        verbose_name='ФИО',
        max_length=255,
        blank=True,
    )

    content = models.TextField(
        verbose_name='Контент',
        blank=True,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.title
