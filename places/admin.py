from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Picture


# Register your models here.

class PictureInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    readonly_fields = ['headshot_image']
    ordering = ['number']
    extra = 1
    fields = ['image', 'headshot_image']
    
    def headshot_image(self, obj):
        return format_html('<img src="{}" style="max-height: {height}px";>',
                           mark_safe(obj.image.url),height=200)    

    headshot_image.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
