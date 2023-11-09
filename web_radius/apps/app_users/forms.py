from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdminRadiusForm(UserCreationForm):

    username = forms.CharField(max_length=100, min_length=5, required=False, help_text='Enter username')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class AdminRadiusForm2(forms.ModelForm):
    username = forms.CharField(max_length=100, min_length=5, required=False, help_text='Enter username')
    class Meta:
        model = User
        fields = ('username', 'password')

from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class RADIUSAuthenticationForm(AuthenticationForm):
    def __init__(self, realm, request, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.realm = realm

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if self.realm and username and password:
            self.user_cache = authenticate(realm=self.realm,
            username=username,
            password=password)
        if self.user_cache is None:
            raise forms.ValidationError(
            'Please enter a correct username and password. '
            'Note that both fields are case-sensitive.')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('This account is inactive.')
            self.check_for_test_cookie()
        return self.cleaned_data

    def get_user(self):
        return self.user_cache