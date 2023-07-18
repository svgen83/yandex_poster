from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Agency, Picture


# Register your models here.

class PictureInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Picture
    readonly_fields = ['headshot_image']
    ordering = ['number']
    extra = 1
    fields = ['image', 'headshot_image']
    
    def headshot_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')    

    headshot_image.short_description = 'Preview'


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
