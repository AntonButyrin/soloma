from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.auth.models import Group
from singlemodeladmin import SingleModelAdmin

from . import models

admin.site.unregister(Group)


class SliderInLineAdmin(
        SortableInlineAdminMixin,
        admin.TabularInline,
):
    model = models.Slider
    extra = 0


@admin.register(models.SliderPreference)
class SliderPreferenceAdmin(SingleModelAdmin):
    inlines = [SliderInLineAdmin]
