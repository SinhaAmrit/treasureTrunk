from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "formSignupUsername",
                "placeholder": "Username",
                "required": "True",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "formSignupEmail",
                "placeholder": "Email",
                "required": "True",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fakePassword",
                "id": "formSignupPassword",
                "placeholder": "Password",
                "required": "True",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control fakePassword",
                "id": "formSignupConfirmPassword",
                "placeholder": "Confirm Password",
                "required": "True",
            }
        )
    )

    class Meta:
        model = User
        fields = ["email", "username"]
