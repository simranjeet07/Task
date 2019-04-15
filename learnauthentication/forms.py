from django import forms
from .models import RegisterUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
        widgets = {'email': forms.widgets.EmailInput, 'password': forms.widgets.PasswordInput,
        'confirm_password': forms.widgets.PasswordInput}