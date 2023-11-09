from django.contrib.auth.models import User
from django.db import models


class AdminsRadiusModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    username = models.CharField(max_length=100, null=False, blank=False, verbose_name='username')
    created_user = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
class UsersLogsTableModel(models.Model):
    username = models.ForeignKey(AdminsRadiusModel, on_delete=models.CASCADE)
    change = models.CharField(max_length=5000)
    datetime = models.DateTimeField(auto_now_add=True)

class UsersModel(models.Model):
    username = models.CharField(max_length=100)
    ad_group = models.CharField(blank=True, null=True, max_length=300)

    def __str__(self):
        return self.username