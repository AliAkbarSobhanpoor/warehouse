from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


from base.forms import BaseForm
from user.models import Customer
from user.variables import ROLES


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


class StorekeeperLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.storekeeper = get_user_model().objects.get(is_active=True, is_superuser=True, customer_profile__role=ROLES[2][0])
        except get_user_model().DoesNotExist:
            self.storekeeper = None

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        if self.storekeeper is None:
            raise forms.ValidationError("انبار دار یافت نشد")
        user = authenticate(username=self.storekeeper.username, password=password)
        if user is None:
            raise forms.ValidationError("رمز وارد شده اشتباه است.")
        return cleaned_data