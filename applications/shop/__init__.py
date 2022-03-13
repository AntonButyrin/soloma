default_app_config = 'applications.shop.apps.ShopConfig'

class PaymentStatus:
    PENDING = 'pending'
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'

    CHOICES = [
        (PENDING, 'Создан'),
        (WAITING_FOR_CAPTURE, 'На подтверждении'),
        (SUCCEEDED, 'Завершён'),
        (CANCELED, 'Отменён'),
    ]
