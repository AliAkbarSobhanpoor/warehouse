from django import forms

from warehouse.models import Product
from base.forms import BaseForm

class ProductAdminForm(BaseForm):
    class Meta:
        model = Product
        fields = ["name", "price_label", "shell_item_count"]
