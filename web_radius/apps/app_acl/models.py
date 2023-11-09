from django.db import models

from apps.app_users.models import AdminsRadiusModel


class Aclname(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    class Meta:
        db_table = 'aclname'
        managed = True
        verbose_name = 'acl'
        verbose_name_plural = 'acls'

class Adgroupname(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    group_name = models.CharField(max_length=100)
    name_acl = models.ForeignKey(Aclname, on_delete=models.CASCADE, related_name="adgroup_aclname")
    modified_by = models.ForeignKey(AdminsRadiusModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ADGROUPNAME'
        verbose_name_plural = 'ADGROUPNAMES'
        managed = True
        db_table = 'adgroupname'

    def __str__(self):
        return self.name_acl.name

    def __repr__(self):
        return self.name_acl.name



class Aclmodel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    rule_choices = [('permit', 'permit'), ('deny', 'deny')]
    rule = models.CharField(max_length=100, default='permit', choices=rule_choices)
    src = models.CharField(max_length=100, default='any')
    dst = models.CharField(max_length=100)
    port = models.CharField(max_length=100, default=None, blank=True, null=True)
    modified_by = models.ForeignKey(AdminsRadiusModel, on_delete=models.CASCADE)
    name_acl = models.ForeignKey(Aclname, on_delete=models.CASCADE, related_name='aclrule_aclname')
    choices = [
        ('tcp', 'tcp'),
        ('udp', 'udp'),
        ('icmp', 'icmp'),
        ('null', 'ip')
    ]

    proto = models.CharField(max_length=200, choices=choices, default=None, null=True)
    description = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.acl_name.name

    class Meta:
        verbose_name = 'Acl rule'
        verbose_name_plural = 'Acl rules'
        managed = True
        db_table = 'acl'


class IdecoRequestModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(default=None, null=True, blank=True, max_length=1000)
    data = models.CharField(max_length=100000000000)

    def __str__(self):
        return str(self.created)

    class Meta:
        managed = True
        db_table = 'ideco_requests'
        verbose_name = 'Ideco Request'
        verbose_name_plural = 'Ideco Requests'


