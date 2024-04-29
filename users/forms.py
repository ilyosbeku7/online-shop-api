from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    confirmation_code = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'confirmation_code')