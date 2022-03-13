from django.db import models

from ..core.models import PathAndRename, Single


class Preference(Single):
    """ Настройки """

    site_title = models.CharField(
        verbose_name='Название сайта',
        max_length=200,
        blank=True,
    )

    site_description = models.TextField(
        verbose_name='Описание сайта',
        blank=True,
    )

    site_photo = models.ImageField(
        verbose_name='Фотография сайта',
        upload_to=PathAndRename('main/preference/site_photo'),
        help_text='Загружать JPG с размерами 1200x630px',
        blank=True,
    )

    phone = models.TextField(
        verbose_name='Список телефонов',
        help_text='Каждый телефон с новой строки',
    )

    email = models.CharField(
        verbose_name='Эл.почта',
        max_length=100,
    )

    address = models.TextField(
        verbose_name='Адрес',
    )  # yapf: disable

    header_html = models.TextField(
        verbose_name='HEAD',
        help_text='Вставка html-кода для всех страниц сайта перед закрывающимся тегом HEAD',
        blank=True,
    )

    footer_html = models.TextField(
        verbose_name='FOOTER',
        help_text='Вставка html-кода для всех страниц сайта перед закрывающимся тегом FOOTER',
        blank=True,
    )

    social_facebook = models.CharField(
        verbose_name='Facebook',
        max_length=300,
        blank=True,
    )

    social_vkontakte = models.CharField(
        verbose_name='Vkontakte',
        max_length=300,
        blank=True,
    )

    social_instagram = models.CharField(
        verbose_name='Instagram',
        max_length=300,
        blank=True,
    )

    social_telegram = models.CharField(
        verbose_name='Telegram',
        max_length=300,
        blank=True,
    )

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return 'Настройки'
