from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

from ..core.admin import CommonAdmin
from . import models


@admin.register(models.EventBlock)
class EventBlockAdmin(SingleModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(
        SortableAdminMixin,
        CommonAdmin,
):
    list_display = [
        'title',
        'created',
    ]
