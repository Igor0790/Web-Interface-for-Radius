from rest_framework import serializers

from apps.app_acl import models


class AclSerializer(serializers.ModelSerializer):

    #name_acl = serializers.SlugField()
    class Meta:
        model = models.Aclmodel
        fields = ['rule', 'src', 'dst', 'port', 'proto']
        #exclude = ['id', 'modified', 'created', 'modified_by', 'name_acl']

class AdgroupSerializer(serializers.ModelSerializer):
    name_acl = serializers.SlugField()
    class Meta:
        model = models.Adgroupname
        exclude = ['id',  'modified', 'created', 'modified_by']


