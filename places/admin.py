from django.contrib import admin
from .models import Agency, Picture
from django.utils.safestring import mark_safe


# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture
    readonly_fields = ['headshot_image']
    
    def headshot_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')    
    headshot_image.short_description = 'Preview'


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    readonly_fields = ['headshot_image']
    fields = ('number', 'agency_title', 'headshot_image')

    def headshot_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')
    
    headshot_image.short_description = 'Preview'

