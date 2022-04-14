from django.contrib import admin

from .models import ItArea, Technology


class SummarySubjectItAreaInline(admin.TabularInline):
    model = ItArea.technologies.through
    extra = 1


@admin.register(Technology)
class SummarySubjectAdmin(admin.ModelAdmin):
    inlines = [
        SummarySubjectItAreaInline
    ]


@admin.register(ItArea)
class ItAreaAdmin(admin.ModelAdmin):
    inlines = [
        SummarySubjectItAreaInline
    ]
