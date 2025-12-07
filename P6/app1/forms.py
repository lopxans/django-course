from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    