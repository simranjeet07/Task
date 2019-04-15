from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)

