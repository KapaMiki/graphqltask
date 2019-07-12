from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from graphene_django.forms.mutation import DjangoModelFormMutation
from .schema import UserType

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'first_name', 
            'last_name'
        )


class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)

    class Meta:
        form_class = UserUpdateForm
