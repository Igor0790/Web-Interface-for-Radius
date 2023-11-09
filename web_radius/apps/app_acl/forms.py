from django import forms

from apps.app_acl import models

class AdgroupnameForm(forms.Form):

    name_acl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    group_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ('group_name', 'name_acl')



class AdgroupnameForm2(forms.ModelForm):

    name_acl = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    group_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = models.Adgroupname
        fields = ('group_name', 'name_acl')

class AclNameForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = models.Aclname
        fields = ['name']

class AclmodelForm(forms.ModelForm):

    class Meta:
        model = models.Aclmodel
        exclude = ('id', 'modified_by', 'created', 'modified')
        widgets = {
            'rule': forms.Select(attrs={'class': 'custom-select'}),
            'src': forms.TextInput(attrs={'class': 'form-control'}),
            'dst': forms.TextInput(attrs={'class': 'form-control'}),
            'port': forms.TextInput(attrs={'class': 'form-control'}),
            'name_acl': forms.Select(attrs={'class': 'custom-select'}),
            'proto': forms.Select(attrs={'class': 'custom-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }



