from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=False)
    password = forms.CharField()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()