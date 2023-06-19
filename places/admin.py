from django.contrib import admin
from .models import Agency, Picture

# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    inlines = [PictureInline]


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass

