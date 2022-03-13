from decimal import Decimal

from django.db import models

from ..menu import models as delivery_models


class Cart(models.Model):
    """ Корзина """

    is_ordering = models.BooleanField(
        verbose_name='Заказ оформлен?',
        default=False,
    )

    uuid = models.CharField(
        verbose_name='UUID',
        max_length=255,
        unique=True,
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def add(self, product, quantity=1) -> None:
        cart_item_variant = self.items.filter(product=product).first()
        if cart_item_variant:
            cart_item_variant.quantity += quantity
            cart_item_variant.save()
        else:
            CartItem.objects.create(
                cart=self,
                product=product,
                quantity=quantity,
            )

    def remove(self, product) -> None:
        self.items.filter(product=product).delete()

    def clear(self) -> None:
        self.items.all().delete()

    def amount(self) -> Decimal:
        amount = 0
        for item in self.items.all():
            amount += item.product.price * item.quantity
        return amount
    amount.short_description = 'Сумма' # yapf: disable

    def __str__(self) -> str:
        return f'Корзина №{self.id}'


class CartItem(models.Model):
    """ Деталь корзины """

    cart = models.ForeignKey(
        verbose_name='Корзина',
        to=Cart,
        on_delete=models.CASCADE,
        related_name='items',
    )

    product = models.ForeignKey(
        verbose_name='Товар',
        to=delivery_models.Product,
        on_delete=models.CASCADE,
        related_name='+',
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=1,
    )

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'

    @property
    def total(self):
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return f'{self.quantity} шт'


class Order(models.Model):
    """ Заказ """

    uuid = models.CharField(
        verbose_name='UUID',
        max_length=255,
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )

    phone = models.CharField(
        verbose_name='Телефон',
        max_length=255,
    )

    address = models.CharField(
        verbose_name='Адрес',
        max_length=255,
    )

    message = models.TextField(
        verbose_name='Сообщение',
        blank=True,
    )

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    amount = models.CharField(
        verbose_name='Сумма',
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self) -> str:
        return f'Заказ №{self.id}'


class OrderItem(models.Model):
    """ Деталь заказа """

    order = models.ForeignKey(
        verbose_name='Заказ',
        to=Order,
        on_delete=models.CASCADE,
        related_name='items',
    )

    product = models.ForeignKey(
        verbose_name='Товар',
        to=delivery_models.Product,
        on_delete=models.CASCADE,
        related_name='+',
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=1,
    )

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'

    @property
    def total(self):
        return self.quantity * self.product.price

    def __str__(self) -> str:
        return f'{self.quantity} шт'
