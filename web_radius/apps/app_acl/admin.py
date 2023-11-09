from django.contrib import admin
from apps.app_acl.models import IdecoRequestModel

@admin.register(IdecoRequestModel)
class IdecoRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'url', 'data']