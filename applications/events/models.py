import uuid

from django.db import models

from ..core.models import Common, Single


def generate_code(length=10):
    return uuid.uuid4().hex[:length]


class EventBlock(Single):
    """ Настройки мероприятий """

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    content = models.TextField(
        verbose_name='Описание',
    ) # yapf:disable

    class Meta:
        verbose_name = 'настройки мероприятия'
        verbose_name_plural = 'настройки мероприятия'

    def __str__(self):
        return 'настройки мероприятия'


class Event(Common):
    """ Событие """

    title = models.CharField(
        verbose_name='Название',
        max_length=50,
    )

    date = models.CharField(
        verbose_name='Дата',
        max_length=255,
        help_text='Любая формулировка',
    )

    content = models.TextField(
        verbose_name='Описание',
    ) # yapf:disable

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self):
        return self.title
