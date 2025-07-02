from django.contrib import admin
from .models import Product
from base.admin import BaseModelAdmin
from . import forms
from .functions import get_available_stock_level

@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    form = forms.ProductAdminForm
    list_display = (
        "name",
        "price_label",
        "shell_item_count",
        "created_at",
        "stock_level"
    )
    def stock_level(self, obj: Product):
        return get_available_stock_level(obj.id)
    stock_level.short_description = "موجودی انبار"
    search_fields = ("name",)