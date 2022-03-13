import uuid

from django.db import models

from ..core.models import Common, PathAndRename, Single


def generate_code(length=10):
    return uuid.uuid4().hex[:length]


class MenuBlock(Single):
    """ Настройки меню """

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    content = models.TextField(
        verbose_name='Описание',
    ) # yapf:disable

    class Meta:
        verbose_name = 'настройки меню'
        verbose_name_plural = 'настройки меню'

    def __str__(self):
        return 'настройки меню'


class Category(Common):
    """ Категория """

    title = models.CharField(
        verbose_name='Название',
        max_length=50,
    )

    is_meat = models.BooleanField(
        verbose_name='Мясная продукция?',
        default=False,
    )

    is_drinks = models.BooleanField(
        verbose_name='Напитки?',
        default=False,
    )

    is_vegan = models.BooleanField(
        verbose_name='Овощи?',
        default=False,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'категория'
        verbose_name_plural = 'категория'

    def __str__(self):
        return self.title


class Product(Common):
    """ Продукт """

    uuid = models.UUIDField(
        verbose_name='UUID',
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    category = models.ForeignKey(
        verbose_name='Категория',
        to=Category,
        on_delete=models.CASCADE,
        related_name='products',
    )

    title = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=PathAndRename('menu/product/image'),
    )

    content = models.TextField(
        verbose_name='Контент',
    ) # yapf:disable

    price = models.IntegerField(
        verbose_name='Цена',
    ) # yapf:disable

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        default=0,
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукт'

    def __str__(self):
        return self.title
