from django import forms
from .models import Tweet


class CreateTweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['body']
