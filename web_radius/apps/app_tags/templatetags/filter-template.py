from django import template
from apps.app_acl.models import Aclname, Aclmodel
from django.db.models import Count
register = template.Library()



@register.filter
def filter_value(value, args):
    aclname = Aclname.objects.filter(name=args).first()
    return value.filter(name_acl__name=aclname).order_by('id')


@register.filter
def count_acl(aclname):
    count = Aclmodel.objects.filter(name_acl=aclname).count()
    return count

