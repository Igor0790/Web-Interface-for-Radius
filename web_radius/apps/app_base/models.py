from django.db import models
from apps.app_users.models import UsersModel




class Radusergroup(models.Model):
    username = models.ForeignKey(UsersModel, default=None, on_delete=models.CASCADE)
    groupname = models.TextField()
    priority = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'radusergroup'

    def __str__(self):
        return self.groupname

class Dictionary(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    attribute = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=64, blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    vendor = models.CharField(max_length=32, blank=True, null=True)
    recommendedop = models.CharField(max_length=32, blank=True, null=True)
    recommendedtable = models.CharField(max_length=32, blank=True, null=True)
    recommendedhelper = models.CharField(max_length=32, blank=True, null=True)
    recommendedtooltip = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictionary'

class Nas(models.Model):
    nasname = models.TextField()
    shortname = models.TextField(blank=True, null=True, default='None')
    type = models.TextField(blank=True, null=True, default='Other')
    ports = models.IntegerField(blank=True, null=True, default=None)
    secret = models.TextField(blank=True, null=True)
    server = models.TextField(blank=True, null=True, default=None)
    community = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)


    class Meta:
        managed = True
        db_table = 'nas'


class Radacct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.TextField()
    acctuniqueid = models.TextField(unique=True)
    username = models.TextField(blank=True, null=True)
    realm = models.TextField(blank=True, null=True)
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.TextField(blank=True, null=True)
    nasporttype = models.TextField(blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctupdatetime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctinterval = models.BigIntegerField(blank=True, null=True)
    acctsessiontime = models.BigIntegerField(blank=True, null=True)
    acctauthentic = models.TextField(blank=True, null=True)
    connectinfo_start = models.TextField(blank=True, null=True)
    connectinfo_stop = models.TextField(blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.TextField(blank=True, null=True)
    callingstationid = models.TextField(blank=True, null=True)
    acctterminatecause = models.TextField(blank=True, null=True)
    servicetype = models.TextField(blank=True, null=True)
    framedprotocol = models.TextField(blank=True, null=True)
    framedipaddress = models.GenericIPAddressField(blank=True, null=True)
    framedipv6address = models.GenericIPAddressField(blank=True, null=True)
    framedipv6prefix = models.GenericIPAddressField(blank=True, null=True)
    framedinterfaceid = models.TextField(blank=True, null=True)
    delegatedipv6prefix = models.GenericIPAddressField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'radacct'


class Radcheck(models.Model):
    username = models.ForeignKey(UsersModel, default=None, on_delete=models.CASCADE)
    attribute = models.TextField()

    choices = [
        ('=', '='),
        ('==', '=='),
        ('>=', '>='),
        ('<=', '<=>'),
        (':=', ':='),
        ('+=', '+='),
        ('!=', '!='),
        ('=~', '=~'),
        ('=*', '=*'),
        ('!*', '!*'),
        ('+', '+')
    ]

    op = models.CharField(max_length=2, choices=choices)
    value = models.TextField()
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'radcheck'


class Radgroupcheck(models.Model):
    groupname = models.ForeignKey(Radusergroup, default=None, on_delete=models.CASCADE)
    attribute = models.TextField()
    choices = [
        ('=', '='),
        ('==', '=='),
        ('>=', '>='),
        ('<=', '<=>'),
        (':=', ':='),
        ('+=', '+='),
        ('!=', '!='),
        ('=~', '=~'),
        ('=*', '=*'),
        ('!*', '!*'),
        ('+', '+')
    ]

    op = models.CharField(max_length=2, choices=choices)
    value = models.TextField()
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'radgroupcheck'


class Radgroupreply(models.Model):
    groupname = models.ForeignKey(Radusergroup, default=None, on_delete=models.CASCADE)
    attribute = models.TextField()
    choices = [
        ('=', '='),
        ('==', '=='),
        ('>=', '>='),
        ('<=', '<=>'),
        (':=', ':='),
        ('+=', '+='),
        ('!=', '!='),
        ('=~', '=~'),
        ('=*', '=*'),
        ('!*', '!*'),
        ('+', '+')
    ]

    op = models.CharField(max_length=2, choices=choices)
    value = models.TextField()
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'radgroupreply'


class Radhuntgroup(models.Model):
    groupname = models.TextField()
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'radhuntgroup'
        managed = True


class Radpostauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    reply = models.TextField(blank=True, null=True)
    calledstationid = models.TextField(blank=True, null=True)
    callingstationid = models.TextField(blank=True, null=True)
    authdate = models.DateTimeField()
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        db_table = 'radpostauth'
        managed = True


class Radreply(models.Model):
    username = models.ForeignKey(UsersModel, default=None, on_delete=models.CASCADE)
    attribute = models.TextField()
    choices = [
        ('=', '='),
        ('==', '=='),
        ('>=', '>='),
        ('<=', '<=>'),
        (':=', ':='),
        ('+=', '+='),
        ('!=', '!='),
        ('=~', '=~'),
        ('=*', '=*'),
        ('!*', '!*'),
        ('+', '+')
    ]

    op = models.CharField(max_length=2, choices=choices)
    value = models.TextField()
    modified = models.DateTimeField(blank=True, null=True, auto_now=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)


    class Meta:
        db_table = 'radreply'
        managed = True

