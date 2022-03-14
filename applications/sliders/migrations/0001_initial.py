# Generated by Django 4.0.2 on 2022-02-25 13:54

import applications.core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='published', max_length=50, verbose_name='Статус')),
                ('image', models.ImageField(upload_to=applications.core.models.PathAndRename('sliders/slider/image'), verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'слайдеры',
                'verbose_name_plural': 'слайдеры',
            },
        ),
        migrations.CreateModel(
            name='SliderPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('content', models.TextField(help_text='Для того,чтобы выделить написать внутри тега <a></a>', verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'настройки блока слайдер',
                'verbose_name_plural': 'настройки блока слайдер',
            },
        ),
    ]