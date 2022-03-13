# Generated by Django 4.0.2 on 2022-03-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='address',
            field=models.TextField(default='Белгород, Белгородский район, Таврово - 4, улица Северная, 19', verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preference',
            name='email',
            field=models.CharField(default='solomarest@yandex.ru', max_length=100, verbose_name='Эл.почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preference',
            name='phone',
            field=models.TextField(default='+7 (4722) 400-477', help_text='Каждый телефон с новой строки', verbose_name='Список телефонов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preference',
            name='social_facebook',
            field=models.CharField(blank=True, max_length=300, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='preference',
            name='social_instagram',
            field=models.CharField(blank=True, max_length=300, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='preference',
            name='social_telegram',
            field=models.CharField(blank=True, max_length=300, verbose_name='Telegram'),
        ),
        migrations.AddField(
            model_name='preference',
            name='social_vkontakte',
            field=models.CharField(blank=True, max_length=300, verbose_name='Vkontakte'),
        ),
    ]
