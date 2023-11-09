from django.contrib import admin
from apps.app_users.models import AdminsRadiusModel, UsersModel



@admin.register(AdminsRadiusModel)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'username']

@admin.register(UsersModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'ad_group']

