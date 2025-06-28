from django import forms

from warehouse.models import Product, WarehouseItem
from base.forms import BaseForm

class ProductAdminForm(BaseForm):
    class Meta:
        model = Product
        fields = ["name", "price_label", "shell_item_count", "sell_price"]

class WarehouseItemAdminForm(BaseForm):
    class Meta:
        model = WarehouseItem
        fields = ["product", "stock_level"]