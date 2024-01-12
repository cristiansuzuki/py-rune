from django import forms
from .models import *

class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = ('nick')
        widgets = {
            'nick':forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleFirstName', 'placeholder': 'Nickname'})
        }
