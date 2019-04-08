from django import forms
from .models import User, TwitterUser


class CreateUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password']


class CreateTwitterUserForm(forms.ModelForm):

    class Meta:
        model = TwitterUser
        fields = ['user']
