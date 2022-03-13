import telebot
from django.conf import settings


def send_telegram(obj) -> str:

    try:
        bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
        channel_id = f'-100{settings.TELEGRAM_CHAT_ID}'
        text = f'\n *Заказ №:* {obj.pk} \n \n *Имя:* {obj.name} \n \n *Телефон:* {obj.phone} \n \n *Адрес:* {obj.address}'
        if obj.message:
            text += f'\n \n *Комментарий:* {obj.message}'
        message = bot.send_message(
            chat_id=channel_id,
            text=text,
            parse_mode='Markdown',
        )

        get_id = message.message_id
        post_address = f'https://t.me/c/{settings.TELEGRAM_CHAT_ID}/{get_id}'
        return post_address
    except Exception:
        return None
