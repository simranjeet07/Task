from .models import Login
from django import forms
import re
from django.core.validators import URLValidator

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        widgets={'username': forms.widgets.TextInput, 'password': forms.widgets.PasswordInput, 'email': forms.widgets.EmailInput}


class UrlForm(forms.Form):
    url = forms.CharField(validators=[URLValidator()])
    name = forms.CharField(widget=forms.TextInput)

    