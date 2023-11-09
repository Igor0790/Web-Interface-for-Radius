from apps.app_base.models import Nas, Radhuntgroup, Radcheck, Radreply, Radusergroup, Radgroupreply, Radgroupcheck, Radpostauth, \
    Dictionary
from django import forms



class NasFormModel(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nasname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    secret = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    shortname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Nas
        fields = ['description', 'nasname', 'secret', 'shortname']


class RadhuntgroupForm(forms.ModelForm):
    groupname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nasipaddress = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nasportid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Radhuntgroup
        exclude = ['id']

class RadcheckForm(forms.ModelForm):

    class Meta:
        model = Radcheck
        exclude = ['id']
        widgets = {
            'username': forms.Select(attrs={'class': 'custom-select'}),
            'attribute': forms.TextInput(attrs={'class': 'form-control'}),
            'op': forms.Select(attrs={'class': 'custom-select'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})

        }

class RadreplyForm(forms.ModelForm):
    class Meta:
        model = Radreply
        exclude = ['id']
        widgets = {
            'username': forms.Select(attrs={'class': 'custom-select'}),
            'attribute': forms.TextInput(attrs={'class': 'form-control'}),
            'op': forms.Select(attrs={'class': 'custom-select'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})

        }

class RadusergroupForm(forms.ModelForm):
    class Meta:
        model = Radusergroup
        exclude = ['id']
        widgets = {
            'username': forms.Select(attrs={'class': 'custom-select'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'groupname': forms.TextInput(attrs={'class': 'form-control'})
        }

class RadgroupreplyForm(forms.ModelForm):
    class Meta:
        model = Radgroupreply
        exclude = ['id', 'created', 'modified']
        widgets = {
            'groupname': forms.Select(attrs={'class': 'custom-select'}),
            'attribute': forms.TextInput(attrs={'class': 'form-control'}),
            'op': forms.Select(attrs={'class': 'custom-select'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})

        }

class RadgroupcheckForm(forms.ModelForm):
    class Meta:
        model = Radgroupcheck
        exclude = ['id', 'created', 'modified']
        widgets = {
            'groupname': forms.Select(attrs={'class': 'custom-select'}),
            'attribute': forms.TextInput(attrs={'class': 'form-control'}),
            'op': forms.Select(attrs={'class': 'custom-select'}),
            'value': forms.TextInput(attrs={'class': 'form-control'})

        }

class RadpostauthForm(forms.ModelForm):
    class Meta:
        model = Radpostauth
        exclude = ['id']

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        exclude = ['id']

class DictionaryFindForm(forms.Form):
    find_word = forms.CharField()
    class Meta:
        include = ['find_word']