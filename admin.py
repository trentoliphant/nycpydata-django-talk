from django.contrib import admin
from .models import UIPermission

@admin.register(UIPermission)
class UIPermissionAdmin(admin.ModelAdmin):
    exclude = ('content_type',)
    list_display = ('name','codename')

