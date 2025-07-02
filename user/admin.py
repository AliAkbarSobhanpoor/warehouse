from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from base.admin import BaseModelAdmin
from warehouse.functions import get_customer_total_price
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomerAdminForm
from user.models import Customer


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(Customer)
class CustomerAdmin(BaseModelAdmin):
    form = CustomerAdminForm
    list_display = [
        'first_name',
        'last_name',
        'role',
        'total_credit',
    ]
    def total_credit(self, obj):
        return get_customer_total_price(obj.id)
    total_credit.short_description = "اعتبار کل"