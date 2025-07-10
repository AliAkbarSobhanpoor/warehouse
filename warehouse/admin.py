from django.contrib import admin
from .models import Product
from base.admin import BaseModelAdmin
from . import forms
from .functions import get_available_stock_level
from .variables import PRODUCT_TABLE_FIELD


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    form = forms.ProductAdminForm
    list_display = (*PRODUCT_TABLE_FIELD,)

    def stock_level(self, obj: Product):
        return get_available_stock_level(obj.id, None)
    stock_level.short_description = "موجودی انبار"
    search_fields = ("name",)