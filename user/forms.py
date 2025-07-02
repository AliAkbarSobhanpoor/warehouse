from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from base.forms import BaseForm
from user.models import Customer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

class CustomerAdminForm(BaseForm):
    class Meta:
        model = Customer
        fields = (
            "user",
            "first_name",
            "last_name",
            'role'
        )