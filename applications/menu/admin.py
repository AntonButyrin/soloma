from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from ..core.admin import CommonAdmin
from . import models


@admin.register(models.MenuBlock)
class MenuBlockAdmin(SingleModelAdmin):
    pass


class ProductAdmin(
        SortableInlineAdminMixin,
        admin.TabularInline,
):
    model = models.Product
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(
        SortableAdminMixin,
        CommonAdmin,
):
    list_display = [
        'title',
        'created',
    ]
    inlines = [ProductAdmin]
