from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from ..core import admin as core
from . import models


@admin.register(models.Review)
class ReviewAdmin(
        SortableAdminMixin,
        core.CommonAdmin,
):
    list_display = [
        'title',
        'created',
    ]

    search_fields = [
        'title',
    ]
