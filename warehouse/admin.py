from django.contrib import admin
from .models import Product, WarehouseItem
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
        "sell_price",
        "created_at"
    )

    search_fields = ("name",)


@admin.register(WarehouseItem)
class WarehouseItemAdmin(BaseModelAdmin):
    form = forms.WarehouseItemAdminForm
    list_display = (
        "product",
        "stock_level"
    )

    def stock_level(self, obj: WarehouseItem):
        return get_available_stock_level(obj.product.id)
    stock_level.short_description = "موجودی انبار"
    raw_id_fields = ("product",)
