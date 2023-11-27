from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    telefone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Telefone"}),
    )
