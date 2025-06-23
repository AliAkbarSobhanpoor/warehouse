from django.contrib import admin
from .models import Product, WarehouseItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price_label",
        "sell_price",
    )
    search_fields = ("name",)


@admin.register(WarehouseItem)
class WarehouseItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "stock_level",
    )
    list_filter = ("stock_level",)
    raw_id_fields = ("product",)
