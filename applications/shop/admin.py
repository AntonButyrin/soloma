from django.contrib import admin

from . import models


class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 0
    readonly_fields = [
        'get_product_title',
        'total',
    ]

    def get_product_title(self, obj):
        return obj.product.title
    get_product_title.short_description = 'Название' # yapf: disable


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'number',
        'amount',
    ]
    readonly_fields = [
        'created',
    ]
    inlines = [
        CartItemInline,
    ]

    def number(self, obj):
        return f'Заказ №{obj.id}'
    number.short_description = 'Номер заказа' # yapf: disable


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = [
        'get_product_title',
        'total',
    ]

    def get_product_title(self, obj):
        return obj.product.title
    get_product_title.short_description = 'Название' # yapf: disable

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'address',
    ]
    readonly_fields = [
        'name',
        'phone',
        'address',
        'message',
    ]
    inlines = [
        OrderItemInline,
    ]

    def number(self, obj):
        return f'Заказ №{obj.id}'
    number.short_description = 'Номер заказа' # yapf: disable
