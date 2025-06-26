from django.contrib import admin
from .models import Product, WarehouseItem
from base.admin import BaseModelAdmin
from . import forms


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
        "stock_level",
    )
    list_filter = ("stock_level",)
    raw_id_fields = ("product",)
