from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import ItArea, Skill, Video, Work


class ItAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_description', 'logo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("name",)}

    def get_description(self, obj):
        return obj.description[:10]

    get_description.short_description = "description"


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(ItArea, ItAreaAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Skill, SkillsAdmin)
admin.site.register(Work, WorksAdmin)
