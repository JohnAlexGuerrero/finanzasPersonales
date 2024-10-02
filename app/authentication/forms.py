from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=32, required=True)
    email = forms.CharField(label='email', max_length=52, required=True)
    password = forms.CharField(label='password', max_length=32, required=True, widget=forms.PasswordInput())